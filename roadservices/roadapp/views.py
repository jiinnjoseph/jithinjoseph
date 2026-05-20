
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from . forms import Customregisterform
from . forms import fuelrequest_form
from . forms import servicerequest_form
from . models import UserfuelRequest
from .models import CustomUser
from . models import UserserviceRequest



# Create your views here.

def user_page(request):
    return render(request,'user_page.html')

def login_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:

            login(request, user)
            if user.role == 'user':
                return redirect('success')
            elif user.role == 'worker':
                return redirect('workerfuelview')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        form = Customregisterform(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')

            if CustomUser.objects.filter(username=username).exists():

                messages.error(request, 'Username already exists')
                return render(request, 'signup.html', {'form': form})

            user = form.save(commit=False)
            user.role = form.cleaned_data.get('role')
            user.set_password(form.cleaned_data.get('password1'))
            user.save()

            messages.success(request, 'Account created successfully')
            return redirect('login_page')

    else:
        form = Customregisterform()

    return render(request, 'signup.html', {'form': form})



def Requestfuel_form(request):
    if request.method=="POST":
        obj = fuelrequest_form(request.POST)
        if obj.is_valid:
            obj.save()
             
            messages.success(request,"Request Submitted Successfully!!!")
            return redirect("/roadapp/user-page/")
        return HttpResponse('data added')
    else:
            obj = fuelrequest_form()
    return render(request,'fuel_register.html',{'x':obj})


def customfuelview(request):
    fuel = UserfuelRequest.objects.all()
    return render(request, 'userfuelview.html', {'x': fuel})


def customserviceview(request):

    service = UserserviceRequest.objects.all()
    return render(request, 'userserviceview.html', {'x': service})


def logout_page(request):
    logout(request)
    messages.success(request,"logged out successfully!!! login again!!")
    return redirect('login_page')


def Requestissue_form(request):
    if request.method=="POST":
        obj = servicerequest_form(request.POST,request.FILES)
        if obj.is_valid:
            obj.save()
            messages.success(request,"Request Submitted Successfully!!!")
            return redirect("/roadapp/user-page/")
        return HttpResponse('data added')
    else:
            obj = servicerequest_form()
    return render(request,'issue_register.html',{'x':obj})


@login_required
def worker_fueldashboard(request):
    fuel = UserfuelRequest.objects.filter(
        assigned_worker=request.user,status__in=['pending', 'In progress'])
    if not fuel.exists():
        messages.success(request, "Good Job !! No Pending requests")
        return render(request, 'worker_fuelview.html')
    return render(request, 'worker_fuelview.html', {'x': fuel})



@login_required
def worker_servicedashboard(request):
    service = UserserviceRequest.objects.filter(
        assigned_worker=request.user,status__in=['pending', 'In progress'])
    if not service.exists():
        messages.success(request, "Good Job !! No Pending requests")
        return render(request, 'worker_serviceview.html')
    return render(request, 'worker_serviceview.html', {'x': service})
    



@login_required
def update_fuelstatus(request, id):
    ob = get_object_or_404(UserfuelRequest, id=id)
    if request.method == "POST":
        ob.status = request.POST.get('status')
        ob.save()
        messages.success(request,"status updated successfully ")
    return redirect('workerfuelview')


@login_required
def update_servicestatus(request, id):
    ob = get_object_or_404(UserserviceRequest, id=id)
    if request.method == "POST":
        ob.status = request.POST.get('status')
        ob.save()
    messages.success(request,"status updated successfully ")
    return redirect('workerserviceview')

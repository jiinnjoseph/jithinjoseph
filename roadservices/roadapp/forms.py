from django import forms
from django.contrib.auth.forms  import UserCreationForm
from . models import UserfuelRequest
from . models import UserserviceRequest
from . models import CustomUser
from . models import UserserviceRequest




class Customregisterform(UserCreationForm):

    email=forms.EmailField()
    phone_no =forms.CharField(max_length=20)    
    first_name= forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)


    class Meta:
        model= CustomUser
        fields= ['username','first_name','last_name','email','phone_no','role','password1','password2']

class fuelrequest_form(forms.ModelForm):
    
    class Meta:
        model =  UserfuelRequest
        fields = "__all__"
        exclude = ['status','assigned_worker']

class servicerequest_form(forms.ModelForm):
    
    class Meta:
        model =  UserserviceRequest
        fields = "__all__"
        exclude = ['status','assigned_worker']


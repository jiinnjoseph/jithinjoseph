from django.urls import path
from . import views


urlpatterns = [
    
    path('login_page/',views.login_view,name='login_page'),
    path('user-page/',views.user_page,name='success'),
    path('signup/',views.signup_view,name='signup'),
    path('fuelregister/',views.Requestfuel_form,name="emergency_fuel"),
    path('logout_page/',views.logout_page,name='logout'),
    path('custom_fuelview/',views.customfuelview,name='fuel_requests'),
    path('custom_serviceview/',views.customserviceview,name='service_requests'),
    path('servicerequest/',views.Requestissue_form,name="services"),
    path('workerserviceview/',views.worker_servicedashboard,name='workerserviceview'),
    path('workerfuelview/',views.worker_fueldashboard, name='workerfuelview'),
    path('update-fuelstatus/<int:id>/',views.update_fuelstatus,name='update_fuelstatus'),
    path('update-servicestatus/<int:id>/',views.update_servicestatus,name='update_servicestatus')

]
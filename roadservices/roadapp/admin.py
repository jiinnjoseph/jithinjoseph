from django.contrib import admin
from . models import UserserviceRequest
from . models import UserfuelRequest

# Register your models here.




class MasterAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    def save_model(self, request, obj, form, change):
        obj.created_user = request.user
        return super().save_model(request, obj, form, change)


class Servicerequestadmin(MasterAdmin):
    list_display = ['customer_name','vehicle','issue','location','created_at']

class Fuelrequestadmin(MasterAdmin):
    list_display = ['customer_name','fuel_type','fuel_quantity','location','created_at']

admin.site.register(UserserviceRequest,Servicerequestadmin)
admin.site.register(UserfuelRequest,Fuelrequestadmin)
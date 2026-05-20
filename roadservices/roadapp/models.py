
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('user', 'User'),
        ('worker', 'Worker'),
    )

    role = models.CharField(max_length=10, choices= ROLE_CHOICES,help_text='Select category')
    

class UserfuelRequest(models.Model):

    customer_name = models.CharField(max_length=100)

    FUEL_CHOICES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel')
    ]

    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)
    
    UNIT_CHOICES = [
        ('ml.', 'Milliliter'),
        ('Ltr.', 'Liter'),
    ]

    fuel_quantity = models.IntegerField()

    unit = models.CharField(max_length=5, choices=UNIT_CHOICES)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (

        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),

    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending',)
    assigned_worker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,
    limit_choices_to={'role': 'worker'}
    )

class UserserviceRequest(models.Model):

    customer_name = models.CharField(max_length=100)

    VEHICLE_CHOICES = [
        ('2-Wheeler', '2-wheeler'),
        ('4-Wheeler.', '4-Wheeler'),
        ('4-Wheel above', 'above')
    ]

    vehicle = models.CharField(max_length=20,choices=VEHICLE_CHOICES)

    images = models.ImageField(upload_to='std_img/',blank=True,null=True)

    SERVICE_CHOICES = [
        ('Tyre-Puncher', 'Puncher'),
        ('Starting Issues', 'starting issues'),
        ('Other','other')
    ]

    issue = models.CharField(max_length=20,choices=SERVICE_CHOICES)
    Description = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (

        ('pending', 'Pending'),
        ('in progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='pending')
    assigned_worker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,
    limit_choices_to={'role': 'worker'}
    )


class Master(models.Model):
    isactive = models.BooleanField(default=True)
    


from django.db import models

# Create your models here.

class EmployeeModel(models.Model):

    emp_name = models.CharField(max_length=10,blank=True,null=True,default=None)
    emp_email = models.CharField(unique=True,max_length=8)
    emp_address = models.CharField(max_length=250)
    emp_city = models.CharField(max_length=50)
    emp_created_at = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "employee"


class Registration(models.Model):

    username = models.CharField(max_length=250,blank=True,null=True,default=None)
    email = models.CharField(unique=True,max_length=8)
    country = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=10)
    reg_created_at = models.DateTimeField(auto_now_add=True)
    reg_modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'registration_form'




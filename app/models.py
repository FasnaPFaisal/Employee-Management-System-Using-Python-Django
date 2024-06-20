from django.db import models

# Create your models here.
class AddEmployee(models.Model):
    employee_id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_joining = models.DateField()
    role = models.CharField(max_length=50)
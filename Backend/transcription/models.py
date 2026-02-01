from django.db import models

# Create your models here.

class Roles(models.Model):
    role_name = models.CharField(max_length=50)
    
class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=50)
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)



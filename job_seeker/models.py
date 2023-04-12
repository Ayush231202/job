from django.db import models

# Create your models here.
class Signup(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    E_mail=models.EmailField(max_length=50 , unique=True)
    Pass1=models.CharField(max_length=20)
    City=models.CharField(max_length=10)
    Country=models.CharField(max_length=15)
    Username=models.CharField(max_length=20, unique=True)
    visit_count=models.IntegerField(default=0)

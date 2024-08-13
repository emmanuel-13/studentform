from django.db import models

# Create your models here.
class  StudentModel(models.Model):
    name  = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=0)
    sex = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
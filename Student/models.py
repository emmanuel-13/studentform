from django.db import models

# Create your models here.
class Students(models.Model):
    # class atrribute
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10, choices=(("male", "Male"), ("female", "Female")))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} {self.sex}"
    
    class Meta:
        verbose_name_plural = "Students"
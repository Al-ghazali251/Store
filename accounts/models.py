from django.db import models
from django.contrib.auth.models import User

class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20,default="customer")
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=20)
    phone = models.IntegerField()

    
    def __str__(self):
        return f"{self.user.first_name} details"
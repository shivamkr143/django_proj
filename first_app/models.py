from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=150,unique=True)
    cost  = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class subject(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    fblink = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return  self.user.username
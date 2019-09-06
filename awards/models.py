from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/',null = True)
    user_bio =models.TextField()
    user = models.ForeignKey(User ,null=True)




class Project(models.Model):
    photo = models.ImageField(upload_to= 'images/' , null = True)
    link = models.TextField()
    description =models.TextField(max_length=100 , null=True)
    rating = models.IntegerField(default = 0, null= True)


    

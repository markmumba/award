from django.db import models
from django.contrib.auth.models import User
from tinymce .models import HTMLField
# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/', null=True)
    user_bio = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    projects = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.user
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()



class Project(models.Model):
    title = models.CharField(max_length=89, null= True)
    links = models.CharField(max_length=60)
    description = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(
        upload_to='projects/', default='project_image')

    class Meta:
        ordering = ['-pk']

    @classmethod
    def search_by_title(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return news

    @classmethod
    def print_all(cls):
        project = Project.objects.all()
        return project

    @classmethod
    def get_project(cls, profile):
        project = Project.objects.filter(Profile__pk = profile)
        return project

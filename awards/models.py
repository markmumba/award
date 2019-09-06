from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile/',null = True)
    user_bio =models.TextField()
    user = models.TextField()

    def __str__ (self):
        return self.user





class (models.Model):
    title = models.CharField(max_length = 60)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date =models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', default = 'article_image')


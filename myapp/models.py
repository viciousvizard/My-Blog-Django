from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    job_title= models.CharField(max_length=100)
    pic = models.FileField(upload_to = 'pic')

    def __str__(self):
        return self.location

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

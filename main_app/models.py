from django.db import models
from django.contrib.auth.models import User 

class City(models.Model): 
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=500)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.name 

    class Meta: 
        ordering = ['name']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']


#count -> length of list in db .count django 
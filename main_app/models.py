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




# class Posts(models.Model):

#     name = models.CharField(max_length=100)
#     img = models.CharField(max_length=250)
#     bio = models.TextField(max_length=500)
#     verified_artist = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']


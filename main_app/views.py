from django.shortcuts import render, redirect 
#from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views import View 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login 

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("/")
        else:
            return redirect("signup")

class Profile(TemplateView):
    template_name = "profile.html"




# '''
# class City:
#     def __init__(self, name, bio, img):
#         self.name = name
#         self.bio = bio
#         self.img = img

# cities = [
#     City("New York", "The Big Apple", "pictureUrl"),
#     City("Dallas", "Everything's bigger in Texas", "pictureUrl"),
#     City("San Francisco", "Golden gate bridge", "pictureUrl"),
#     City("Atlanta", "Georgia peaches", "pictureUrl"),
#     City("Boston", "Real New England", "pictureUrl"),
#     City("Miami", "The Sunshine City", "pictureUrl"),
#     City("Las Vegas", "What happens in Vegas!", "pictureUrl"),
#     City("Los Angeles", "The City of Angels", "pictureUrl"),
#     City("Honolulu", "Have a luau", "pictureUrl"),
#     City("St. Louis", "Golden Arches", "pictureUrl"),
#     City("Chicago", "The Windy City", "pictureUrl"),
#     City("London", "See the Big ben Tower", "pictureUrl"),
# ]
# '''

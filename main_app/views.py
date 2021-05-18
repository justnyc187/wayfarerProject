from django.shortcuts import render, redirect 
#from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views import View 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile, Post 
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.views.generic import DetailView 



# Create your views here.

class Home(TemplateView):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "home.html", context)

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #bring in profile and link user here 
            location = request.POST.get("location")
            Profile.objects.create(user = user, location = location) #create new profile object add input in signup form to add location
            login(request,user)
            return redirect("/profile/")
        else:
            context = {"form": form}
            return render(request, "registration/login.html", context)
            

# @method_decorator(login_required, name='dispatch')
class ProfileDetail(TemplateView):
    template_name = "profile.html"

    #access user info + create context - user.name etc. imported user from django 


class ProfileUpdate(UpdateView):
    model = User 
    fields = ['username']
    template_name = "profile_update.html"
    success_url = "/profile/"
    

class PostDetail(DetailView):
    model = Post 
    template_name = "post_detail.html"

    








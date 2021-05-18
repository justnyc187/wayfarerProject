from django.shortcuts import render, redirect 
#from django.views import View # <- View class to handle requests 
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views import View 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile 



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
            user = form.save() #bring in profile and link user here 
            Profile.objects.create(user = user) #create new profile object add input in signup form to add location
            login(request,user)
            return redirect("/profile/")
        else:
            return redirect("signup")

@method_decorator(login_required, name='dispatch')
class Profile(TemplateView):
    template_name = "profile.html"

    #access user info + create context - user.name etc. imported user from django 

        
#{{user.username}}
#name + current city + current profile img  + joindate 











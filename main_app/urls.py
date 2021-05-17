from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup', views.SignUp.as_view(), name="signup"),
    path('profile/', views.Profile.as_view(), name="profile"),
]



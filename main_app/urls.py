from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup', views.SignUp.as_view(), name="signup"),
    path('profile/', views.ProfileDetail.as_view(), name="profile"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
]

from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('account/', include('users_app.urls')),
    path('', include('main_app.urls'))
]





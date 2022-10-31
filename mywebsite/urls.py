from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('service/', include('service.urls')),
    path('contact/', include('contact.urls')),
    path('', views.index),
]

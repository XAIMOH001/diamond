
from django.contrib import admin
from django.urls import path
from  diamondapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('register/', views.register),
    path('About/', views.About),
    path('services/', views.services),
    path('contact/', views.contact),
]

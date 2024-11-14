
from django.contrib import admin
from django.urls import path,include

import diamondapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diamondapp.urls')),
]

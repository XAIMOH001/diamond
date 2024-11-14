from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def About(request):
    return render(request, 'About.html')
def contact(request):
    return render(request, 'contact.html')
def register(request):
    return render(request, 'register.html')
def services(request):
    return render(request, 'services.html')

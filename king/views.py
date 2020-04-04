from django.shortcuts import render

def home(request):
    return render(request, 'king/home.html')
# Create your views here.

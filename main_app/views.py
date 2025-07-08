# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

def feed(request):
    try:
        return render(request, 'feed.html')
    except Exception as e:
        return HttpResponse(f"Error en feed: {str(e)}")

def home(request):
    try:
        return render(request, 'home.html')
    except Exception as e:
        return HttpResponse(f"Error en home: {str(e)}")

def about(request):
    try:
        return render(request, 'about.html')
    except Exception as e:
        return HttpResponse(f"Error en about: {str(e)}")

def services(request):
    try:
        return render(request, 'services.html')
    except Exception as e:
        return HttpResponse(f"Error en services: {str(e)}")

def blog(request):
    try:
        return render(request, 'blog.html')
    except Exception as e:
        return HttpResponse(f"Error en blog: {str(e)}")

def contact(request):
    try:
        return render(request, 'contact.html')
    except Exception as e:
        return HttpResponse(f"Error en contact: {str(e)}")

def custom_404(request, exception):
    return render(request, '404.html', status=404)
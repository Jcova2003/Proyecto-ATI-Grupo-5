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
        notificaciones = [
            {
                "usuario": "Sofía Marcano",
                "mensaje": "le ha dado like a tu publicación.",
                "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQytc93VfA29gwZ4w1ySdWjx1CSJBM6qGG3BA&s"
            },
            {
                "usuario": "Lisangely Goncalves",
                "mensaje": "ha comentado en tu publicación.",
                "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQytc93VfA29gwZ4w1ySdWjx1CSJBM6qGG3BA&s"
            },
            {
                "usuario": "Valeria Ciccolella",
                "mensaje": "le ha dado like a tu publicación.",
                "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQytc93VfA29gwZ4w1ySdWjx1CSJBM6qGG3BA&s"
            },
        ]
        return render(request, 'home.html', {
            'notificaciones': notificaciones
        })
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
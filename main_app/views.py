# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .models import Publicacion
from collections import namedtuple
from datetime import datetime, timezone

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
        usuario = Usuario.objects.get(email="helenaTorres@gmail.com")
        posts = Publicacion.objects.all()
        postList = []
        Post = namedtuple("Post", "usuario contenido multimedia privacidad fecha_creacion reacciones comentarios")

        for p in posts:
            time = datetime.now(timezone.utc) - p.fecha_creacion
            x = Post(p.usuario, p.contenido, p.multimedia, p.privacidad, time, "14k", 10)
            postList.append(x)

        Friends = namedtuple("Friend", "usuario active lastActive")
        friends = Usuario.objects.all()
        friendList = []
        i = 1
        for f in friends:
            if f.nombre != usuario.nombre: 
                x = Friends(f, i != 3, "10min")
                friendList.append(x)
                i=i+1

        return render(request, 'home.html', {
            'notificaciones': notificaciones,
            'user' : usuario,
            'posts': postList,
            'friendList': friendList
        })
    except Exception as e:
        return HttpResponse(f"Error en home: {str(e)}")

def notifications(request):
    try:
        # This is sample data - in a real app, you would fetch this from a database
        all_notifications = [
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://i.pinimg.com/736x/82/47/0b/82470b4ed44c3edacfcd4201e2297050.jpg",
                "action": "ha comentado en tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
                "action": "ha comentado en tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Sofia Marcano",
                "user_image": "https://cdn.pixabay.com/photo/2016/03/31/19/56/avatar-1295397_640.png",
                "action": "le ha dado like a tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
                "action": "ha comentado en tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
                "action": "ha comentado en tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
                "action": "ha comentado en tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
                "action": "ha comentado en tu publicación.",
            },
            {
                "user_name": "Lisangely Goncalves",
                "user_image": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D",
                "action": "ha comentado en tu publicación.",
            },
        ]
        count = int(request.GET.get("count", 5))  # Mostrar 5 por defecto
        notifications = all_notifications[:count]
        return render(
            request,
            "notificationsTemplate.html",
            {"notifications": notifications, "count": count},
        )
    except Exception as e:
        return HttpResponse(f"Error en notifications: {str(e)}")

def chat_with_friend(request):
    # Aquí puedes agregar lógica para obtener datos del amigo o mensajes
    context = {
        "friend_name": 'Belén Cruz',
        # Puedes agregar más datos que necesites pasar a la plantilla
    }
    return render(request, "chatTemplate.html", context)

def login(request):
    try:
        return render(request, "login.html")
    except Exception as e:
        return HttpResponse(f"Error en login: {str(e)}")

def register(request):
    try:
        return render(request, "register.html")
    except Exception as e:
        return HttpResponse(f"Error en register: {str(e)}")

def profile(request):
    try:
        return render(request, "profile.html")
    except Exception as e:
        return HttpResponse(f"Error en profile: {str(e)}")

def custom_404(request, exception):
    return render(request, "404.html", status=404)

# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Usuario
from .models import Publicacion
from .utils import get_notifications, build_post_list, build_friend_list


def home(request):
    try:
        notificaciones = get_notifications()
        usuario = Usuario.objects.get(email="helenaTorres@gmail.com")
        posts = Publicacion.objects.all()
        postList =  build_post_list(posts)
        friendList = build_friend_list(usuario)

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

def profile(request, id_usuario = None):
    try:
        notificaciones = get_notifications()
        logged_user = Usuario.objects.get(email="helenaTorres@gmail.com") 
       
        profile_user = (
            get_object_or_404(Usuario, id=id_usuario)
            if id_usuario and id_usuario != logged_user.id
            else logged_user
        )

        posts = Publicacion.objects.filter(usuario=profile_user).order_by('-fecha_creacion')
        postList = build_post_list(posts)
        friendList = build_friend_list(logged_user)

        return render(request, 'profile.html', {
            'notificaciones': notificaciones,
            'user' : profile_user,
            'posts': postList,
            'friendList': friendList,
            'logged_user': logged_user
        })

    except Exception as e:
        return HttpResponse(f"Error en profile: {str(e)}")

def custom_404(request, exception):
    return render(request, "404.html", status=404)

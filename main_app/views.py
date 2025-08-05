# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Usuario
from .models import Publicacion, Comentario
from .utils import get_notifications, build_post_list, build_friend_list
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


def home(request):
    try:
        notificaciones = get_notifications()
        usuario = Usuario.objects.get(email="helenaTorres@gmail.com")
        posts = Publicacion.objects.all()
        postList =  build_post_list(posts)
        friendList = build_friend_list(usuario)

        if request.method == "POST":
            contenido = request.POST['post-text']
            multimedia = request.POST['post-mlt']

            new_post = Publicacion(usuario = usuario, contenido = contenido, multimedia = multimedia)
            new_post.save()

        return render(
            request,
            "feedTemplate.html",
            {
                "notificaciones": notificaciones,
                "user": usuario,
                "posts": postList,
                "friendList": friendList,
                "numFriends": len(friendList)
            },
        )
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
        "friend_name": "Belén Cruz",
        # Puedes agregar más datos que necesites pasar a la plantilla
    }
    return render(request, "chatTemplate.html", context)


def login(request):
    try:
        return render(request, "login.html")
    except Exception as e:
        return HttpResponse(f"Error en login: {str(e)}")


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
        numFriends = len(build_friend_list(profile_user))

        return render(request, 'profile.html', {
            'notificaciones': notificaciones,
            'user' : profile_user,
            'posts': postList,
            'friendList': friendList,
            'numFriends': numFriends,
            'logged_user': logged_user
        })

    except Exception as e:
        return HttpResponse(f"Error en profile: {str(e)}")

def post(request, id_publicacion):
    try:
        notificaciones = get_notifications()
        logged_user = Usuario.objects.get(email="helenaTorres@gmail.com")
        post = (
            get_object_or_404(Publicacion, id = id_publicacion)
        )
        # post = Publicacion.objects.get(id = 1)
        friendList = build_friend_list(logged_user)
        comments = Comentario.objects.filter(publicacion = post)

        return render(
            request,
            "detailedPostTemplate.html",
            {
                "notificaciones": notificaciones,
                "user": logged_user,
                "post": post,
                "friendList": friendList,
                "numFriends": len(friendList),
                "comments": comments,
                "numComments": comments.count()
            },
        )
    except Exception as e:
        return HttpResponse(f"Error en home: {str(e)}")

def custom_404(request, exception):
    return render(request, "404.html", status=404)


def register(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not nombre or not email or not password1 or not password2:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, "register.html")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, "register.html")

        # Check if email already exists
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado.")
            return render(request, "register.html")

        try:
            # Create user - ci field is now nullable so we don't need to provide it
            user = Usuario.objects.create_user(
                email=email, password=password1, nombre=nombre
            )
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("login")

        except Exception as e:
            messages.error(request, f"Error al registrar usuario: {str(e)}")
            return render(request, "register.html")

    return render(request, "register.html")

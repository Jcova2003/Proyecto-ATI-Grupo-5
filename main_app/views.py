# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Usuario
from .models import Publicacion, Comentario, Notificacion
from .utils import get_notifications, build_post_list, build_friend_list, save_post, build_feed_queryset, build_wall_queryset
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, "login.html")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  
            return redirect("home")
        else:
            messages.error(request, "Correo o contraseña incorrectos.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    try:
        usuario = request.user
        
        save_post(request, usuario)

        notificaciones = get_notifications(usuario)
        posts = build_feed_queryset(usuario)
        postList =  build_post_list(posts)
        friendList = build_friend_list(usuario)

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
        usuario = request.user # O usar request.user si tienes auth
        count = int(request.GET.get("count", 5))
        all_notifications = get_notifications(usuario)[:count]

        return render(
            request,
            "notificationsTemplate.html",
            {"notifications": all_notifications, "count": count},
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

def profile(request, id_usuario = None):
    try:
        logged_user = request.user
        
        save_post(request, logged_user)

        notificaciones = get_notifications(logged_user)
       
        profile_user = (
            get_object_or_404(Usuario, id=id_usuario)
            if id_usuario and id_usuario != logged_user.id
            else logged_user
        )

        if profile_user == logged_user and id_usuario is not None:
            return redirect("my_profile")

        posts = build_wall_queryset(profile_user, logged_user)
        postList = build_post_list(posts)
        friendList = build_friend_list(logged_user)
        isMyFriend = any(friend.usuario.id == profile_user.id for friend in friendList)
        numFriends = len(build_friend_list(profile_user))

        return render(request, 'profile.html', {
            'notificaciones': notificaciones,
            'user' : profile_user,
            'posts': postList,
            'friendList': friendList,
            'numFriends': numFriends,
            'logged_user': logged_user,
            'isMyFriend': isMyFriend
        })

    except Exception as e:
        return HttpResponse(f"Error en profile: {str(e)}")

def post(request, id_publicacion):
    try:
        logged_user = request.user
        post = (
            get_object_or_404(Publicacion, id = id_publicacion)
        )
        
        notificaciones = get_notifications(logged_user)

        if request.method == "POST":
            comment_content = request.POST["comment"]
            new_comment = Comentario(
                publicacion=post,
                usuario=logged_user,
                contenido=comment_content
            )
            new_comment.save()
            
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
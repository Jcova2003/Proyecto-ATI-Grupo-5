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
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.utils.translation import gettext as _

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            messages.error(request, _("Todos los campos son obligatorios."))
            return render(request, "login.html")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)  
            return redirect("home")
        else:
            messages.error(request, _("Correo o contraseña incorrectos."))

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




# views.py
def chats_view(request):
    logged_user = request.user
    friendList = build_friend_list(logged_user)
    users = Usuario.objects.all()
    users_data = []

    for user in users:
        users_data.append({
            "id": user.id,  # Add this line!
            "name": user.nombre or user.email,
            "avatar": user.foto.url if user.foto else "/static/img/default_profile.png",
            "last_message": "¡Hola! Este es un mensaje de prueba.",
            "last_time": "hace 1 min",
        })

    return render (
            request,
            "chatsTemplate.html",
            {
                "users": users_data,
                "friendList": friendList,
                "notificaciones": get_notifications(logged_user),
            },
        )

def chat_with_friend(request):
    logged_user = request.user
    friendList = build_friend_list(request.user)
    friend_id = request.GET.get("friend_id")
    friend = None
    if friend_id:
        try:
            friend = Usuario.objects.get(id=friend_id)
        except Usuario.DoesNotExist:
            pass
    if not friend:
        return render(request, "chatTemplate.html", {
            "friend_name": "Usuario no encontrado",
            "friend_first_name": "Usuario",
            "friend_avatar": "/static/img/default_profile.png",
        })
    full_name = friend.nombre or friend.email
    first_name = full_name.split()[0] if full_name else ""
    return render(request, "chatTemplate.html", {
        "friend_name": full_name,
        "friend_avatar": friend.foto.url if friend.foto else "/static/img/default_profile.png",
        "friend_first_name": first_name,
        "friendList": friendList,
        "notificaciones": get_notifications(logged_user),
    })

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
    
@login_required
def editProfile(request):
    user = request.user
    notificaciones = get_notifications(user)
    friendList = build_friend_list(user)

    try:
        if request.method == 'POST':
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            descripcion = request.POST.get("descripcion")
            foto = request.FILES.get('foto', None)
            
            if Usuario.objects.filter(email=email).exclude(pk=user.pk).exists():
                messages.error(request, _("El correo electrónico ya está registrado por otro usuario."))
                return redirect('edit_profile')
    
            if password1 and password1 != password2:
                messages.error(request, _("Las contraseñas no coinciden."))
                return redirect('edit_profile')

            user.nombre = nombre
            user.email = email
            user.descripcion = descripcion

            if password1:
                user.set_password(password1)
                update_session_auth_hash(request, user)

            if foto:
                user.foto = foto

            user.save()
            messages.success(request, _("Perfil actualizado correctamente."))
            return redirect('edit_profile')  

        return render(request, 'editProfile.html', {
            'notificaciones': notificaciones,
            'friendList': friendList,
            'user': user,  
        })

    except Exception as e:
        return HttpResponse(f"Error en edit-profile: {str(e)}")

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
            messages.error(request, _("Todos los campos son obligatorios."))
            return render(request, "register.html")

        if password1 != password2:
            messages.error(request, _("Las contraseñas no coinciden."))
            return render(request, "register.html")

        # Check if email already exists
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, _("El correo electrónico ya está registrado por otro usuario."))
            return render(request, "register.html")

        try:
            # Create user - ci field is now nullable so we don't need to provide it
            user = Usuario.objects.create_user(
                email=email, password=password1, nombre=nombre
            )
            messages.success(request, _("Registro exitoso. Ahora puedes iniciar sesión."))
            return redirect("login")

        except Exception as e:
            messages.error(request, f"Error al registrar usuario: {str(e)}")
            return render(request, "register.html")

    return render(request, "register.html")
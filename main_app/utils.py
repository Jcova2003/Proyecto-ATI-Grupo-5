# main_app/utils.py
from collections import namedtuple
from datetime import datetime, timezone
from .models import Usuario, Comentario, Publicacion

def get_notifications():
    return [
        {
            "usuario": "Emanuel Delgado",
            "mensaje": "le ha dado like a tu publicación.",
            "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQytc93VfA29gwZ4w1ySdWjx1CSJBM6qGG3BA&s"
        },
        {
            "usuario": "Isabel Cárdenas",
            "mensaje": "ha comentado en tu publicación.",
            "avatar_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQytc93VfA29gwZ4w1ySdWjx1CSJBM6qGG3BA&s"
        },
    ]

def get_friends(usuario):
    return Usuario.objects.filter(
        recibidas__de_usuario=usuario,
        recibidas__estado='aceptada'
    ).distinct().union(
        Usuario.objects.filter(
            enviadas__para_usuario=usuario,
            enviadas__estado='aceptada'
        ).distinct()
    )

def build_feed_queryset(user):
    public_posts = Publicacion.objects.filter(privacidad="publico")
    friends = get_friends(user).union(
        Usuario.objects.filter(email=user.email)
    ).values_list('id', flat=True)
    private_posts = Publicacion.objects.filter(privacidad="privado", usuario_id__in=friends)
    posts = (public_posts | private_posts).order_by('-fecha_creacion')
    return posts

def build_wall_queryset(user, logged_user=None):
    public_posts = Publicacion.objects.filter(usuario=user, privacidad="publico")
    private_posts = Publicacion.objects.filter(privacidad="privado")
    friends = get_friends(user).union(
        Usuario.objects.filter(email=user.email)
    )
    if logged_user in friends:
        posts = (public_posts | private_posts).order_by('-fecha_creacion')
    else:
        posts = public_posts.order_by('-fecha_creacion')
    
    return posts

def build_post_list(posts):
    Post = namedtuple("Post", "id usuario contenido multimedia privacidad fecha_creacion reacciones comentarios")
    post_list = []
    for p in posts:
        tiempo = time_format(datetime.now(timezone.utc) - p.fecha_creacion)
        comment_count = Comentario.objects.filter(publicacion = p).count
        post = Post(p.id, p.usuario, p.contenido, p.multimedia, p.privacidad, tiempo, "14k", comment_count)
        post_list.append(post)
    return post_list

def build_friend_list(usuario_actual):
    Friends = namedtuple("Friend", "usuario active lastActive")
    amigos = get_friends(usuario_actual)
    friend_list = []
    i = 1
    for f in amigos:
        x = Friends(f, i != 3, "10min")
        friend_list.append(x)
        i += 1
    return friend_list

def time_format(time):
    segundos = int(time.total_seconds())
    
    if segundos < 60:
        return f"{segundos}seg"
    minutos = segundos // 60
    if minutos < 60:
        return f"{minutos}min"
    horas = minutos // 60
    if horas < 24:
        return f"{horas}h"
    dias = horas // 24
    if dias < 30:
        return f"{dias}d"
    meses = dias // 30
    if meses < 12:
        return f"{meses}m"
    anios = meses // 12
    return f"{anios}y"

def save_post(request, usuario):
    if request.method == "POST":
        contenido = request.POST['post-text']
        multimedia = request.POST['post-mlt']
        visibilidad = request.POST['visibility']

        if not contenido and not multimedia:
            raise ValueError("La publicación no puede estar vacía.")
        if visibilidad not in ["publico", "privado"]:
            raise ValueError("Visibilidad no válida. Debe ser 'publico' o 'privado'.")

        new_post = Publicacion(usuario = usuario, contenido = contenido, multimedia = multimedia, privacidad = visibilidad)
        new_post.save()
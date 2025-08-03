# main_app/utils.py
from collections import namedtuple
from datetime import datetime, timezone
from .models import Usuario, Publicacion, SolicitudAmistad

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

def build_post_list(posts_queryset):
    Post = namedtuple("Post", "usuario contenido multimedia privacidad fecha_creacion reacciones comentarios")
    post_list = []
    for p in posts_queryset:
        tiempo = time_format(datetime.now(timezone.utc) - p.fecha_creacion)
        post = Post(p.usuario, p.contenido, p.multimedia, p.privacidad, tiempo, "14k", 10)
        post_list.append(post)
    return post_list

def build_friend_list(usuario_actual):
    Friends = namedtuple("Friend", "usuario active lastActive")
    amigos = Usuario.objects.filter(
            recibidas__de_usuario=usuario_actual,
            recibidas__estado='aceptada'
        ).distinct()
    amigos = Usuario.objects.filter(
            enviadas__para_usuario=usuario_actual,
            enviadas__estado='aceptada'
        ).distinct().union(amigos)
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

# main_app/utils.py
from collections import namedtuple
from datetime import datetime, timezone
from .models import Usuario, Comentario, Notificacion

def get_notifications(usuario):
    notificaciones = Notificacion.objects.filter(usuario=usuario).order_by("-fecha")[:10]
    result = []

    for notif in notificaciones:
        actor = notif.actor if notif.actor else notif.usuario

        # Construir la URL manualmente
        avatar_path = actor.foto  # Esto será 'img/12345678.png'
        avatar_url = f"/static/media/{avatar_path}" if avatar_path else "https://via.placeholder.com/150"

        result.append({
            "usuario": actor.nombre,
            "avatar_url": avatar_url,
            "mensaje": notif.contenido
        })

    return result



def build_post_list(posts_queryset):
    Post = namedtuple("Post", "id usuario contenido multimedia privacidad fecha_creacion reacciones comentarios")
    post_list = []
    for p in posts_queryset:
        tiempo = time_format(datetime.now(timezone.utc) - p.fecha_creacion)
        comment_count = Comentario.objects.filter(publicacion = p).count
        post = Post(p.id, p.usuario, p.contenido, p.multimedia, p.privacidad, tiempo, "14k", comment_count)
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

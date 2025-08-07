# main_app/utils.py
from collections import namedtuple
from datetime import datetime, timezone
from .models import Usuario, Comentario, Publicacion, Notificacion, SolicitudAmistad

def get_notifications(usuario):
    notificaciones = Notificacion.objects.filter(usuario=usuario, leida = False).order_by("-fecha")[:10]
    result = []

    for notif in notificaciones:
        actor = notif.actor if notif.actor else notif.usuario

        # Construir la URL manualmente
        avatar_path = actor.foto  # Esto será 'img/12345678.png'
        avatar_url = f"/static/media/{avatar_path}" if avatar_path else "https://via.placeholder.com/150"

        result.append({
            "usuario": actor.nombre,
            "avatar_url": avatar_url,
            "mensaje": notif.contenido,
            "tipo": notif.tipo,
            "id": notif.id
        })

    return result

def crear_notificacion(usuario_destino, actor, tipo, contenido):
    Notificacion.objects.create(
        usuario=usuario_destino,
        actor=actor,
        tipo=tipo,
        contenido=contenido,
        leida=False,
        enviada_por_correo=False
    )

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
    private_posts = Publicacion.objects.filter(usuario=user,privacidad="privado")
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
    if request.method == "POST" and "post" in request.POST:
        contenido = request.POST['post-text']
        multimedia = request.POST['post-mlt']
        visibilidad = request.POST['visibility']

        if not contenido and not multimedia:
            raise ValueError("La publicación no puede estar vacía.")
        if visibilidad not in ["publico", "privado"]:
            raise ValueError("Visibilidad no válida. Debe ser 'publico' o 'privado'.")

        new_post = Publicacion(usuario = usuario, contenido = contenido, multimedia = multimedia, privacidad = visibilidad)
        new_post.save()

def action_notification(request):
    if request.method == "POST":
            if "accept" in request.POST:
                id = request.POST["accept"]
                notif = Notificacion.objects.get(id=id)
                notif.leida = "True"
                notif.save()
                friendRequest = find_friend_request(notif.actor, notif.usuario)
                if friendRequest:
                    friendRequest.estado = "aceptada"
                    friendRequest.save()
            elif "reject" in request.POST:
                id = request.POST["reject"]
                notif = Notificacion.objects.get(id=id)
                notif.leida = "True"
                notif.save()
                friendRequest = find_friend_request(notif.actor, notif.usuario)
                if friendRequest:
                    friendRequest.estado = "rechazada"
                    friendRequest.save()

def find_friend_request(user1, user2):
    friendRequest_to = SolicitudAmistad.objects.filter(de_usuario=user1, para_usuario=user2)
    friendRequest_from = SolicitudAmistad.objects.filter(de_usuario=user2, para_usuario=user1)
    return friendRequest_to.union(friendRequest_from).first()
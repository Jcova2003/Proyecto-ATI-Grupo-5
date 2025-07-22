# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

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
        usuario = {
                "nombre": "Helena Torres",
                "foto": "/static/img/12345678.png", 
                "email": "valTorres@gmail.com",
                "ci": "12345678",
                "fecha_nacimiento": "23/9/2002",
                "genero": "femenino",
                "descripcion": "Pensamientos ruidosos, ideas claras y playlists que rompen rutinas. 🖤🔥",
                "color_favorito": "magenta",
                "libro_favorito": "- \"Eleanor & Park\" de Rainbow Rowell",
                "musica_favorita": "Punk-Rock",
                "videojuegos_favoritos": "Disco Elysium",
                "password_hash": "123456",
                "configuracion": "",
                "fecha_registro": "22/7/2025",
            }
        
        posts = [
            {
                "usuario": "Emanuel Delgado",
                "foto": "/static/img/12345679.png",
                "contenido": "La verdad es que últimamente me he clavado duro en el desarrollo web. Hay algo increíblemente satisfactorio en ver cómo una idea se convierte en una app funcional, justo ahí, en el navegador. 😎💻\nMe encanta jugar con React y ver cómo los componentes toman vida con solo unas líneas bien pensadas. También estoy metiéndome cada vez más en el backend—Django y Node me tienen intrigado. Me gusta entender cómo se conectan todas las piezas: base de datos, API, frontend… como un rompecabezas que sólo cobra sentido cuando todo fluye.\nY sí, me emociono con cosas como la optimización de carga, diseño responsive y esas pequeñas animaciones que hacen que la experiencia sea más suave. 🎨⚙️✨\nSi alguien quiere intercambiar ideas o hablar sobre sus proyectos locos de apps web, aquí estoy.",
                "reacciones": "70 mil",  
                "comentarios": "500",
                "fecha_creacion": "11 hrs"
            },
            {
                "usuario": "Isabel Cárdenas",
                "foto": "/static/img/12345680.png",
                "contenido": "Docker y yo tenemos una relación complicada. 😅 Cada vez que creo que entendí los contenedores, aparece una red que no conecta, un volumen que no se monta, o un error que me hace cuestionar mi existencia como dev.\nHoy pasé 3 horas peleando con un bind mount... spoiler: era un typo. 🤦‍♀️\nSi alguien tiene tips, rituales mágicos o paciencia infinita para lidiar con estas bestias virtuales, se aceptan abrazos y sugerencias.",
                "reacciones": "2 mil",  
                "comentarios": "350",
                "fecha_creacion": "6 hrs"
            },
            {
                "usuario": "Belén Cruz",
                "foto": "/static/img/12345681.png",
                "contenido": "Los templates de Django son como la mezcla perfecta entre orden y magia ✨. Literalmente te permiten separar el HTML del caos lógico y mantener todo bonito, limpio y funcional. 🙌\nDjango lo tiene bien pensado. 🎯",
                "reacciones": "14",  
                "comentarios": "3",
                "fecha_creacion": "5 min"
            },
        ]
        friendList = [
            {
                "user": "Emanuel Delgado",
                "pfp": "/static/img/12345679.png",
                "active": True,
                "lastActive": ""
            },
            {
                "user": "Isabel Cárdenas",
                "pfp": "/static/img/12345680.png",
                "active": True,
                "lastActive": ""
            },
            {
                "user": "Belén Cruz",
                "pfp": "/static/img/12345681.png",
                "active": False,
                "lastActive": "10 mins"
            },
        ]

        return render(request, 'home.html', {
            'notificaciones': notificaciones,
            'user' : usuario,
            'posts': posts,
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


def custom_404(request, exception):
    return render(request, "404.html", status=404)

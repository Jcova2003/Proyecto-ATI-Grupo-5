# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse


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
        return render(request, 'home.html', {
            'notificaciones': notificaciones
        })
    except Exception as e:
        return HttpResponse(f"Error en home: {str(e)}")


def about(request):
    try:
        return render(request, "about.html")
    except Exception as e:
        return HttpResponse(f"Error en about: {str(e)}")


def services(request):
    try:
        return render(request, "services.html")
    except Exception as e:
        return HttpResponse(f"Error en services: {str(e)}")


def blog(request):
    try:
        return render(request, "blog.html")
    except Exception as e:
        return HttpResponse(f"Error en blog: {str(e)}")


def contact(request):
    try:
        return render(request, "contact.html")
    except Exception as e:
        return HttpResponse(f"Error en contact: {str(e)}")


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


def chat_with_friend(request, friend_name):
    # Aquí puedes agregar lógica para obtener datos del amigo o mensajes
    context = {
        "friend_name": friend_name,
        # Puedes agregar más datos que necesites pasar a la plantilla
    }
    return render(request, "chatTemplate.html", context)


def custom_404(request, exception):
    return render(request, "404.html", status=404)

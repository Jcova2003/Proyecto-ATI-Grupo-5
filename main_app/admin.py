from django.contrib import admin
from django.db import transaction, connection
from .models import Usuario, Publicacion, Notificacion, Comentario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("email", "nombre", "ci", "is_active", "fecha_registro")
    fields = (
        "email", 
        "nombre", 
        "foto", 
        "ci",
        "fecha_nacimiento",
        "genero",
        "descripcion",
        "color_favorito",
        "libro_favorito",
        "musica_favorita",
        "videojuegos_favoritos",
        "is_active",
        "is_staff",
        "is_superuser"
    )

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        # Override the entire form view to disable FK checks
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().changeform_view(
                        request, object_id, form_url, extra_context
                    )
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().changeform_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        # Override the delete view to disable FK checks
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().delete_view(request, object_id, extra_context)
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().delete_view(request, object_id, extra_context)


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "contenido", "fecha_creacion")
    readonly_fields = ("fecha_creacion",)

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().changeform_view(
                        request, object_id, form_url, extra_context
                    )
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().changeform_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        # Override the delete view to disable FK checks for Publicacion deletion
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().delete_view(request, object_id, extra_context)
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().delete_view(request, object_id, extra_context)

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "actor", "tipo", "contenido", "leida", "enviada_por_correo", "fecha")
    fields = ("usuario", "actor", "tipo", "contenido", "leida", "enviada_por_correo", "fecha")
    readonly_fields = ("fecha",)
    list_filter = ("tipo", "leida", "enviada_por_correo", "fecha")
    search_fields = ("usuario__email", "actor__email", "contenido", "tipo")

    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().changeform_view(request, object_id, form_url, extra_context)
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().changeform_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().delete_view(request, object_id, extra_context)
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().delete_view(request, object_id, extra_context)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("publicacion", "usuario", "contenido", "fecha")
    fields = ("publicacion", "usuario", "contenido", "respuesta_a")
    readonly_fields = ("fecha",)
    
    def changeform_view(self, request, object_id=None, form_url="", extra_context=None):
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().changeform_view(request, object_id, form_url, extra_context)
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().changeform_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        if request.method == "POST":
            with connection.cursor() as cursor:
                cursor.execute("PRAGMA foreign_keys=OFF;")
                try:
                    return super().delete_view(request, object_id, extra_context)
                finally:
                    cursor.execute("PRAGMA foreign_keys=ON;")
        return super().delete_view(request, object_id, extra_context)
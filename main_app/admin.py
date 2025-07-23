from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Usuario,
    Publicacion,
    Comentario,
    SolicitudAmistad,
    Chat,
    Mensaje,
    Notificacion,
    Sesion,
    LenguajeProgramacion,
    UsuarioLenguaje,
)


class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ("email", "nombre", "is_staff", "is_active", "fecha_registro")
    list_filter = ("is_staff", "is_active", "genero", "fecha_registro")
    search_fields = ("email", "nombre", "ci")
    ordering = ("email",)

    # Updated fieldsets to include all Usuario model fields
    fieldsets = (
        (None, {"fields": ("email", "password", "nombre")}),
        (
            "Información Personal",
            {"fields": ("ci", "fecha_nacimiento", "genero", "foto", "descripcion")},
        ),
        (
            "Preferencias",
            {
                "fields": (
                    "color_favorito",
                    "libro_favorito",
                    "musica_favorita",
                    "videojuegos_favoritos",
                )
            },
        ),
        ("Configuración", {"fields": ("configuracion",)}),
        (
            "Permisos",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Fechas importantes", {"fields": ("last_login", "fecha_registro")}),
    )

    # Updated add_fieldsets for creating new users
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "nombre",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    # Make fecha_registro read-only since it has a default value
    readonly_fields = ("fecha_registro", "last_login")


# Register other models
@admin.register(LenguajeProgramacion)
class LenguajeProgramacionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "contenido", "privacidad", "fecha_creacion")
    list_filter = ("privacidad", "fecha_creacion")
    search_fields = ("contenido", "usuario__nombre", "usuario__email")
    readonly_fields = ("fecha_creacion",)


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("publicacion", "usuario", "comentario", "fecha")
    list_filter = ("fecha",)
    search_fields = ("comentario", "usuario__nombre")
    readonly_fields = ("fecha",)


@admin.register(SolicitudAmistad)
class SolicitudAmistadAdmin(admin.ModelAdmin):
    list_display = ("de_usuario", "para_usuario", "estado", "fecha")
    list_filter = ("estado", "fecha")
    search_fields = ("de_usuario__nombre", "para_usuario__nombre")
    readonly_fields = ("fecha",)


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("usuario1", "usuario2")
    search_fields = ("usuario1__nombre", "usuario2__nombre")


@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ("chat", "de_usuario", "contenido", "leido", "fecha")
    list_filter = ("leido", "fecha")
    search_fields = ("contenido", "de_usuario__nombre")
    readonly_fields = ("fecha",)


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "tipo", "contenido", "leida", "fecha")
    list_filter = ("tipo", "leida", "fecha")
    search_fields = ("contenido", "usuario__nombre")
    readonly_fields = ("fecha",)


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ("usuario", "activo", "fecha_inicio")
    list_filter = ("activo", "fecha_inicio")
    search_fields = ("usuario__nombre",)
    readonly_fields = ("fecha_inicio",)


# Register the main Usuario model
admin.site.register(Usuario, UsuarioAdmin)

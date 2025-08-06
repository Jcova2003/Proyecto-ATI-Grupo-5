from django.contrib import admin
from django.db import transaction, connection
from .models import Usuario, Publicacion, LenguajeProgramacion, Notificacion


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("email", "nombre", "is_active")
    fields = ("email", "nombre", "foto", "is_active")

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


@admin.register(LenguajeProgramacion)
class LenguajeProgramacionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


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

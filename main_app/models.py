from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.conf.urls.static import static


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=100, blank=True)
    foto = models.ImageField(upload_to='img/', default='img/default_profile.png')
    email = models.EmailField(unique=True)
    # Make ci optional and nullable
    ci = models.CharField(max_length=20, unique=True, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=20, blank=True)
    descripcion = models.TextField(blank=True)
    color_favorito = models.CharField(max_length=20, blank=True)
    libro_favorito = models.CharField(max_length=100, blank=True)
    musica_favorita = models.TextField(blank=True)
    videojuegos_favoritos = models.TextField(blank=True)
    configuracion = models.JSONField(null=True, blank=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nombre or self.email

    def pfp_url(self):
        return f"{settings.MEDIA_URL}{self.foto}"

class LenguajeProgramacion(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    PRIVACIDAD_CHOICES = [
        ("publico", "Público"),
        ("privado", "Privado"),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField(blank=True)
    multimedia = models.TextField(blank=True)  # se puede usar JSONField
    privacidad = models.CharField(
        max_length=10, choices=PRIVACIDAD_CHOICES, default="publico"
    )
    fecha_creacion = models.DateTimeField(default=timezone.now)


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    contenido = models.TextField()
    respuesta_a = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='respuestas')
    fecha = models.DateTimeField(default=timezone.now)


class SolicitudAmistad(models.Model):
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("aceptada", "Aceptada"),
        ("rechazada", "Rechazada"),
    ]
    de_usuario = models.ForeignKey(
        Usuario, related_name="enviadas", on_delete=models.CASCADE
    )
    para_usuario = models.ForeignKey(
        Usuario, related_name="recibidas", on_delete=models.CASCADE
    )
    estado = models.CharField(
        max_length=10, choices=ESTADO_CHOICES, default="pendiente"
    )
    fecha = models.DateTimeField(default=timezone.now)


class Chat(models.Model):
    usuario1 = models.ForeignKey(
        Usuario, related_name="chats_usuario1", on_delete=models.CASCADE
    )
    usuario2 = models.ForeignKey(
        Usuario, related_name="chats_usuario2", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("usuario1", "usuario2")


class Mensaje(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    de_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    contenido = models.TextField()
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(default=timezone.now)


class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones_recibidas')
    actor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True, related_name='notificaciones_emitidas')
    tipo = models.CharField(max_length=50)
    contenido = models.TextField()
    leida = models.BooleanField(default=False)
    enviada_por_correo = models.BooleanField(default=False)
    fecha = models.DateTimeField(default=timezone.now)


class Sesion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token = models.TextField()
    fecha_inicio = models.DateTimeField(default=timezone.now)
    activo = models.BooleanField(default=True)


# Relación muchos a muchos entre usuarios y lenguajes
Usuario.lenguajes = models.ManyToManyField(
    LenguajeProgramacion, through="UsuarioLenguaje"
)


class UsuarioLenguaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    lenguaje = models.ForeignKey(LenguajeProgramacion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("usuario", "lenguaje")

from django.test import TestCase
from django.db import IntegrityError
from main_app.models import (
    Usuario, Publicacion, Comentario,
    SolicitudAmistad, Chat, Mensaje, Notificacion, Sesion
)

class ModeloTests(TestCase):

    def setUp(self):
        self.usuario1 = Usuario.objects.create_user(
            email="lis@gmail.com",
            password="password123",
            nombre="lis",
            ci="30395417"
        )
        self.usuario2 = Usuario.objects.create_user(
            email="val@gmail.com",
            password="password456",
            nombre="val",
            ci="29640094"
        )

    # Verificamos que el método __str__ del modelo Usuario devuelva el nombre si está definido
    def test_str_usuario(self):
        self.assertEqual(str(self.usuario1), "lis")

    # No se puede registrar otro usuario con un email ya existente
    def test_usuario_email_unico(self):
        with self.assertRaises(IntegrityError):
            Usuario.objects.create_user(email="lis@gmail.com", password="otra", ci="29565856")

    # Asegura que el método devuelva la ruta relativa o completa de la imagen
    def test_pfp_url(self):
        url = self.usuario1.pfp_url()
        self.assertTrue(url.startswith("/media/img/"))

    # Publicacion: privacidad por defecto
    def test_publicacion_privacidad_por_defecto(self):
        pub = Publicacion.objects.create(usuario=self.usuario1, contenido="Hola mundo")
        self.assertEqual(pub.privacidad, "publico")

    # Comentario: puede responder a otro
    def test_comentario_respuesta(self):
        pub = Publicacion.objects.create(usuario=self.usuario1, contenido="Post")
        comentario1 = Comentario.objects.create(publicacion=pub, usuario=self.usuario1, contenido="Comentario original")
        comentario2 = Comentario.objects.create(publicacion=pub, usuario=self.usuario2, contenido="Respuesta", respuesta_a=comentario1)
        self.assertEqual(comentario2.respuesta_a, comentario1)

    # Comentario: puede tener múltiples respuestas
    def test_comentario_tiene_respuestas(self):
        pub = Publicacion.objects.create(usuario=self.usuario1, contenido="Post")
        parent = Comentario.objects.create(publicacion=pub, usuario=self.usuario1, contenido="Comentario base")
        reply1 = Comentario.objects.create(publicacion=pub, usuario=self.usuario2, contenido="Respuesta 1", respuesta_a=parent)
        reply2 = Comentario.objects.create(publicacion=pub, usuario=self.usuario2, contenido="Respuesta 2", respuesta_a=parent)
        self.assertEqual(parent.respuestas.count(), 2)

    # SolicitudAmistad: estado por defecto
    def test_solicitud_amistad_estado_por_defecto(self):
        solicitud = SolicitudAmistad.objects.create(de_usuario=self.usuario1, para_usuario=self.usuario2)
        self.assertEqual(solicitud.estado, "pendiente")

    # Chat: no se pueden crear duplicados
    def test_chat_unico(self):
        Chat.objects.create(usuario1=self.usuario1, usuario2=self.usuario2)
        with self.assertRaises(IntegrityError):
            Chat.objects.create(usuario1=self.usuario1, usuario2=self.usuario2)

    # Mensaje: asociación con chat y campo leido por defecto
    def test_mensaje_asociado_a_chat(self):
        chat = Chat.objects.create(usuario1=self.usuario1, usuario2=self.usuario2)
        mensaje = Mensaje.objects.create(chat=chat, de_usuario=self.usuario1, contenido="Hola")
        self.assertEqual(mensaje.chat, chat)
        self.assertFalse(mensaje.leido)

    # Notificacion: valores booleanos por defecto
    def test_notificacion_valores_bool(self):
        notif = Notificacion.objects.create(usuario=self.usuario1, tipo="info", contenido="Mensaje")
        self.assertFalse(notif.leida)
        self.assertFalse(notif.enviada_por_correo)

    # Sesion: campo activo por defecto
    def test_sesion_activa_por_defecto(self):
        sesion = Sesion.objects.create(usuario=self.usuario1, token="abc123")
        self.assertTrue(sesion.activo)


    

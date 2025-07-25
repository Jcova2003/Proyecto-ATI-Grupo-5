from django.test import TestCase

from main_app.models import (
    Usuario, LenguajeProgramacion, Publicacion, Comentario,
    SolicitudAmistad, Chat, Mensaje, Notificacion, Sesion
)

class ModeloTests(TestCase):

    def setUp(self):
        self.usuario1 = Usuario.objects.create(
            nombre="lis",
            email="lis@gmail.com",
            ci="30395417",
            password_hash="hash1"
        )
        self.usuario2 = Usuario.objects.create(
            nombre="val",
            email="val@gamil.com",
            ci="29640094",
            password_hash="hash2"
        )

    # Tests for Usuario model: verificamos que el metodo str del modelo Usuario devuelva el nombre si esta definido
    def test_str_usuario(self):
        self.assertEqual(str(self.usuario1), "lis")

    #Que no se puede registrar otro usuario con un email ya existente
    def test_usuario_email_unico(self):
        with self.assertRaises(Exception):
            Usuario.objects.create(email="lis@gmail.com", ci="29565856", password_hash="hash")

    # Tests for LenguajeProgramacion model: verificamos que el nombre del lenguaje se guarde correctamente y sea unico
    def test_crear_lenguaje_unico(self):
        LenguajeProgramacion.objects.create(nombre="Python")
        with self.assertRaises(Exception):
            LenguajeProgramacion.objects.create(nombre="Python")

    # Tests for Publicacion model: verificamos que la privacidad por defecto sea "publico"
    def test_publicacion_privacidad_por_defecto(self):
        pub = Publicacion.objects.create(usuario=self.usuario1, contenido="Hola mundo")
        self.assertEqual(pub.privacidad, "publico")

    # Tests for Comentario model: verificamos que un comentario pueda ser una respuesta a otro
    def test_comentario_respuesta(self):
        pub = Publicacion.objects.create(usuario=self.usuario1, contenido="Publicacion")
        comentario1 = Comentario.objects.create(publicacion=pub, usuario=self.usuario1, contenido="Comentario original")
        comentario2 = Comentario.objects.create(publicacion=pub, usuario=self.usuario2, contenido="Respuesta", respuesta_a=comentario1)
        self.assertEqual(comentario2.respuesta_a, comentario1)

    # Tests for SolicitudAmistad model: verificamos que el estado por defecto sea "pendiente"
    def test_solicitud_amistad_estado_por_defecto(self):
        solicitud = SolicitudAmistad.objects.create(de_usuario=self.usuario1, para_usuario=self.usuario2)
        self.assertEqual(solicitud.estado, "pendiente")

    # Tests for Chat model: verificamos que no se puedan crear chats duplicados entre los mismos usuarios
    def test_chat_unico(self):
        Chat.objects.create(usuario1=self.usuario1, usuario2=self.usuario2)
        with self.assertRaises(Exception):
            Chat.objects.create(usuario1=self.usuario1, usuario2=self.usuario2)

    # Tests for Mensaje model: verificamos que un mensaje se asocie correctamente a un chat y que el campo leido sea False por defecto
    def test_mensaje_asociado_a_chat(self):
        chat = Chat.objects.create(usuario1=self.usuario1, usuario2=self.usuario2)
        mensaje = Mensaje.objects.create(chat=chat, de_usuario=self.usuario1, contenido="Hola")
        self.assertEqual(mensaje.chat, chat)
        self.assertFalse(mensaje.leido)


    # Tests for Notificacion model: verificamos que una notificacion se cree correctamente y que los valores booleanos tengan el valor por defecto
    def test_notificacion_valores_bool(self):
        notif = Notificacion.objects.create(usuario=self.usuario1, tipo="info", contenido="Mensaje")
        self.assertFalse(notif.leida)
        self.assertFalse(notif.enviada_por_correo)

    # Tests for Sesion model: verificamos que una sesion se cree correctamente y que el campo activo sea True por defecto
    def test_sesion_activa_por_defecto(self):
        sesion = Sesion.objects.create(usuario=self.usuario1, token="abc123")
        self.assertTrue(sesion.activo)

    

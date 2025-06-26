from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Proyecto ATI - Grupo 5</title>
    </head>
    <body>
        <h1>¡Bienvenido al Proyecto ATI!</h1>
        <h2>Grupo 5</h2>
        <p>✅ Django funcionando correctamente</p>
        <p>✅ PostgreSQL conectado</p>
        <p>✅ Docker Compose ejecutándose</p>
        <hr>
    </body>
    </html>
    """)
# proyecto_ati/urls.py (archivo principal del proyecto)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # Habilita cambio de idioma vía /i18n/setlang/
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
)

# Configuración para servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # También servir desde STATICFILES_DIRS
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    
# Configurar el handler para errores 404
handler404 = 'main_app.views.custom_404'
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar Apache y mod_wsgi
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        apache2 \
        apache2-dev \
        gcc \
        python3-dev \
    && pip install --no-cache-dir mod_wsgi \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . /app/

# Generar archivos estáticos de Django
RUN python manage.py collectstatic --noinput

# Copiar configuración de Apache
COPY ./apache/django.conf /etc/apache2/sites-available/django.conf

# Deshabilitar el sitio por defecto y habilitar el de Django
RUN a2dissite 000-default \
    && a2ensite django

# Configurar mod_wsgi
RUN mod_wsgi-express install-module > /etc/apache2/mods-available/wsgi.load \
    && a2enmod wsgi

# Crear directorio de logs si no existe
RUN mkdir -p /var/log/apache2

# Establecer permisos correctos para archivos estáticos
RUN chmod -R 755 /app/staticfiles/ \
    && chmod -R 755 /app/main_app/static/ \
    && chown -R www-data:www-data /app/staticfiles/ \
    && chown -R www-data:www-data /app/main_app/static/

EXPOSE 8000

# Comando para iniciar Apache
CMD ["apache2ctl", "-D", "FOREGROUND"]
# Proyecto-ATI-Grupo-5
## Integrantes
* Valeria Ciccolella
* Jesús Cova
* Samuel Flores
* Lisangely Goncalves
* Sofía Marcano
* Javier Darder

---

## 🚀 Guía rápida para ejecutar el proyecto con Docker

Sigue estos pasos si quieres ejecutar el proyecto rápidamente en tu máquina local usando Docker y **SQLite**:

```bash
# 1. Clona este repositorio
git clone https://github.com/Jcova2003/Proyecto-ATI-Grupo-5.git
cd Proyecto-ATI-Grupo-5

# 2. Copia el archivo de entorno (si es necesario)
cp .env.example .env

# 3. Levanta los servicios con Docker
docker-compose up --build

# 4. Abre el navegador en
http://localhost:8000
```

---

## Integración Continua

Este proyecto utiliza GitHub Actions para CI:

- **Tests**: Se ejecutan automáticamente en cada push o pull request a la rama main.

---

## Comandos Docker para desarrollo

```bash
# Construir y ejecutar con Docker Compose (desarrollo)
docker-compose up --build

# Ejecutar en background
docker-compose up -d

# Ver logs
docker-compose logs -f web

# Ejecutar comandos en el contenedor web
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic

# Detener servicios
docker-compose down

# Detener y eliminar volúmenes (¡CUIDADO! Borra la BD SQLite)
docker-compose down -v
```

---

> **Nota:**  
> Este proyecto usa SQLite como base de datos por defecto, por lo que no necesitas instalar ni configurar PostgreSQL ni usar el archivo `docker-compose.prod.yml`.


---

## Modelo de dominio
![Diagrama de modelo de dominio](/doc/ModeloDominio.png)

---
## Diagrama de casos de uso
![Diagrama de casos de uso](/doc/DiagramaCasoUso.png)

---
## Mapa de navegación
![Mapa de navegación](/doc/NavigationMap.png)

---
## Diagrama de Arquitectura de Sistema
![Diagrama de Arquitectura de Sistema](/doc/diagramaArquitecturaSistema.png)

---
## Diagrama de paquetes
![Diagrama de paquetes](/doc/PackageDiagram.png)

---
## Diagrama de Clase de Analisis 1: Agregar amigo
![Agregar amigo](/doc/diagramaClaseAnalisisAgregarAmigo.png)

---
## Diagrama de Clase de Analisis 2: Chatear
![Chatear](/doc/DiagramaClaseAnalisisChatear.png)

---
## Diagrama de Clase de Analisis 3: Publicar
![Publicar](/doc/DiagramaClaseAnalisisPublicar.png)


# Proyecto-ATI-Grupo-5
## Integrantes
* Valeria Ciccolella
* Jesús Cova
* Samuel Flores
* Lisangely Goncalves
* Sofía Marcano
* Javier Darder


## Integración Continua

Este proyecto utiliza GitHub Actions para CI/CD:

### Workflow automático
- **Tests**: Se ejecutan automáticamente en cada push/PR
- **Build**: Construcción de imagen Docker en rama main
- **Deploy**: Despliegue automático a staging (rama main)

### Comandos Docker para desarrollo

```bash
# Construir y ejecutar con Docker Compose (desarrollo)
docker-compose up --build

# Ejecutar para producción (con archivo separado)
docker-compose -f docker-compose.prod.yml up --build

# Solo construir
docker-compose build

# Ejecutar en background
docker-compose up -d

# Ver logs
docker-compose logs -f web
docker-compose logs -f db

# Ejecutar comandos en el contenedor web
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic

# Detener servicios
docker-compose down

# Detener y eliminar volúmenes (¡CUIDADO! Borra la BD)
docker-compose down -v

# Sin Docker (requiere PostgreSQL local)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
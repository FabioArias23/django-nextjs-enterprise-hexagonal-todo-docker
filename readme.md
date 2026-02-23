# Django & Next.js Enterprise Todo App - Hexagonal Architecture

Este repositorio contiene una aplicación de gestión de tareas de nivel **Senior**, diseñada bajo los estándares de **Clean Architecture** y **Arquitectura Hexagonal**. El enfoque principal es demostrar un sistema altamente desacoplado, escalable y testeable.

🔗 **Repositorio:** [https://github.com/FabioArias23/django-nextjs-enterprise-hexagonal-todo-docker](https://github.com/FabioArias23/django-nextjs-enterprise-hexagonal-todo-docker)

## 🛠️ Stack Tecnológico

- **Backend:** Django 6.0 + Django Rest Framework (DRF)
- **Frontend:** Next.js 15+ (React), TypeScript, Tailwind CSS
- **Base de Datos:** PostgreSQL 15
- **Contenedores:** Docker & Docker Compose
- **Autenticación:** JWT (SimpleJWT) - Ready para Auth0

## 🧠 Arquitectura Senior Implementada

### 1. Backend: Clean Architecture (Hexagonal)
A diferencia del patrón estándar de Django, este proyecto separa las responsabilidades en capas claras:
- **Domain:** Definición de entidades y contratos (`ITaskRepository`). Independiente de cualquier framework.
- **Application:** Casos de uso (`ToggleTaskDoneUseCase`) que contienen la lógica de negocio pura.
- **Infrastructure:** Implementación de persistencia con Django ORM y configuración de adaptadores de entrada/salida.

### 2. Frontend: Repository Pattern
- Desacoplamiento total de la API. Los componentes de React no realizan `fetch` directamente.
- Uso de **Path Mapping** en TypeScript (`@/domain`, `@/infrastructure`) para una navegación limpia entre módulos.
- Centralización de la lógica de datos en repositorios, permitiendo cambiar la fuente de datos sin afectar la UI.

### 3. Dockerización Pro
- Orquestación de servicios mediante **Docker Compose**.
- Uso de redes internas aisladas para la comunicación entre Django y PostgreSQL.
- Volúmenes persistentes para la base de datos, garantizando que los datos no se pierdan al reiniciar contenedores.

## 🚀 Guía de Inicio Rápido

Siga estos pasos para levantar el entorno completo de desarrollo:

### Requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

### Instalación y Despliegue
1. **Clonar el proyecto:**
   ```bash
   git clone https://github.com/FabioArias23/django-nextjs-enterprise-hexagonal-todo-docker.git
   cd django-nextjs-enterprise-hexagonal-todo-docker

   Levantar la infraestructura con Docker:

   docker-compose up --build

   # Crear las tablas en PostgreSQL
docker-compose exec backend python manage.py migrate

Backend (Django):
Entra a la carpeta: cd backend
Activa el entorno virtual: venv\Scripts\activate (Windows)
Instala dependencias: pip install -r requirements.txt
Inicia el server:
python manage.py runserver


Para un perfil Senior, es fundamental saber manejar los servicios de forma independiente, ya sea para hacer debugging específico o para ahorrar recursos.
Aquí tienes los comandos para levantarlos de forma singular usando Docker (recomendado) y de forma local (en tu Windows).
🐳 1. Levantarlos singularmente con DOCKER (Recomendado)
Desde la raíz del proyecto (nextjs-django-crud):
Solo el Backend y la Base de Datos:
(Útil para probar la API con Postman o Insomnia sin cargar el frontend)
code
Bash
docker-compose up db backend
Solo el Frontend:
(Nota: Fallará si el backend no está encendido, pero sirve para ver la UI)
code
Bash
docker-compose up frontend
Ejecutar comandos dentro de un servicio encendido:
code
Bash
# Correr migraciones
docker-compose exec backend python manage.py migrate

# Crear superusuario
docker-compose exec backend python manage.py createsuperuser

# Entrar a la consola de Django
docker-compose exec backend python manage.py shell
💻 2. Levantarlos singularmente de forma LOCAL (Sin Docker)
Nota: Para que el backend funcione localmente, la base de datos de Docker DEBE estar encendida (docker-compose up db).
Backend (Django):
Entra a la carpeta: cd backend
Activa el entorno virtual: venv\Scripts\activate (Windows)
Instala dependencias: pip install -r requirements.txt
Inicia el server:

python manage.py runserver


(Gracias a la lógica que pusimos en settings.py, detectará que estás en local y usará el puerto 5499 de la DB).

Frontend (Next.js):

Entra a la carpeta: cd frontend
Instala dependencias: npm install

Inicia el server:

npm run dev

.venv\Scripts\Activate.ps1

python manage.py runserver
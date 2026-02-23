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


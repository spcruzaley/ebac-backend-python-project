## ¿Cómo Funciona el Entorno Virtual?

Un entorno virtual es una carpeta que contiene una copia de Python y un conjunto de herramientas, bibliotecas y scripts independientes de otros entornos virtuales y de la instalación global de Python en tu sistema.

## Pasos Detallados

**1. Crear y Activar el Entorno Virtual**

Primero, crea el entorno virtual y luego actívalo. Los comandos para crear y activar un entorno virtual son:
```shell
# Crear un entorno virtual llamado "myenv"
python3 -m venv myenv    # En sistemas Unix/Mac
python -m venv myenv     # En sistemas Windows

# Activar el entorno virtual
source myenv/bin/activate    # En sistemas Unix/Mac
myenv\Scripts\activate       # En sistemas Windows
```

Al activar el entorno virtual, cualquier instalación de paquetes (_usando `pip`, por ejemplo_) se realizará dentro de este entorno, sin afectar la instalación global de Python.

**2. Instalar Django y Crear el Proyecto**

Con el entorno virtual activado, instala Django y crea tu proyecto y aplicaciones:
```shell
# Instalar Django en el entorno virtual
pip install django

# Crear un nuevo proyecto Django llamado "myproject"
django-admin startproject myproject

# Navegar al directorio del proyecto
cd myproject

# Crear una nueva aplicación dentro del proyecto
python manage.py startapp myapp
```

**3. Trabajar en el Proyecto**

Mientras el entorno virtual esté activado, puedes ejecutar comandos de Django, instalar más paquetes, y desarrollar tu proyecto.

**4. Desactivar el Entorno Virtual**

Cuando termines de trabajar en tu proyecto, puedes desactivar el entorno virtual para volver al entorno de Python global de tu sistema. Para desactivarlo, simplemente ejecuta:
```shell
deactivate
```

## Resumen de Comandos

```shell
# Crear y activar el entorno virtual
python3 -m venv myenv
source myenv/bin/activate       # Unix/Mac
myenv\Scripts\activate          # Windows

# Instalar Django
pip install django

# Crear un nuevo proyecto Django
django-admin startproject myproject

# Navegar al directorio del proyecto y ejecutar el servidor
cd myproject
python manage.py runserver

# Crear una nueva aplicación
python manage.py startapp myapp

# Desactivar el entorno virtual cuando termines
deactivate
```

## Notas Adicionales
- **Mantén tu entorno virtual activado mientras trabajas en el proyecto:** Esto asegura que todas las dependencias se instalen y utilicen desde el entorno virtual, evitando conflictos con otras versiones de paquetes en tu sistema.
- **Reactivación del entorno virtual:** Si cierras tu terminal o deseas continuar trabajando en tu proyecto en otra sesión, simplemente navega a la carpeta del entorno virtual y actívalo nuevamente usando los comandos de activación.

# Crear modelos

Para crear componentes de bases de datos como tablas, será necesario crear los modelos correspondientes, en este ejemplo veremos la creación de un modelo llamado `Direcciones` en el cual almacenaremos **nombre** y **dirección**.

1. Configurar Django REST Framework en el Proyecto

Añade `rest_framework` a tu lista de aplicaciones instaladas en `settings.py`:
```python
# ejemploEcommerce/settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'ecommerce',  # Asegúrate de que tu aplicación también está aquí
]
```

**2. Crear el Modelo de Dirección**

Define el modelo de dirección en `models.py` de tu aplicación:
```python
# ecommerce/models.py
from django.db import models

class Direccion(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
```

**3. Crear y Aplicar Migraciones**

Crea y aplica las migraciones para crear la tabla en la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate
```
**4. Crear un Serializador**

Crea un serializador para el modelo `Direccion` en `serializers.py`:
```python
# ecommerce/serializers.py
from rest_framework import serializers
from .models import Direccion

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'
```

## Errores comúnes

### Instalación del módulo `rest_framwork`

En caso de obtener un error del siguiente tipo:
```shell
  ...
  ...
ModuleNotFoundError: No module named 'rest_framework'
```
Se deberá actualizar `pip` e instalar el módulo correspondiente mediante los siguientes comandos
```shell
# Actualizar pip
pip install --upgrade pip

# Instalar el modulo
pip install djangorestframework
```
# Proyecto Django

## Requerimientos Mínimos
- **Python** 3.8 o superior
- **pip** (el gestor de paquetes de Python)
- **Virtualenv** (recomendado para crear entornos virtuales aislados)
- **Django** (el framework web)

## Programas a Utilizar
- **Python**: [Descargar aquí](https://www.python.org/downloads/)
- **pip**: Incluido con Python
- **Virtualenv**: Se puede instalar usando pip
- **Django**: Se puede instalar usando pip

## Pasos para Ejecutar el Proyecto
**1. Instalar Python**

Asegúrate de tener Python instalado. Puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).

**2. Clonar este repositorio**

```bash
$ git clone https://github.com/spcruzaley/ebac-backend-python-project.git
```
Entra al directorio descargado
```bash
$ cd ebac-backend-python-project
```

**2. Crear un Entorno Virtual**

Es una buena práctica trabajar en un entorno virtual para mantener las dependencias de tu proyecto aisladas. Para instalar `virtualenv` si no lo tienes ya:
```shell
pip install virtualenv
```
Luego, crea un entorno virtual y actívalo:
```shell
# En sistemas Unix/Mac
python3 -m venv myenv
source myenv/bin/activate

# En sistemas Windows
python -m venv myenv
myenv\Scripts\activate
```
Revisa [esta información](documentacion/ENTORNO_VIRTUAL.MD) adicional sobre entornor virutales.

**3. Instalar Django y demás dependencias**

Con el entorno virtual activado, instala Django utilizando pip:
```shell
pip install django
pip install djangorestframework
```

**4. Ejecutar el proyecto**

Ahora el proyecto ya tiene todo lo necesario para ser ejecutado correctamente, por lo que solo tendrás que iniciarlo con el siguiente comando
```bash
$ python ejemploEcommerce/manage.py runserver
```

Una vez terminado de ejecutar el proyecto, detenerlo con las teclas `Ctrl + C` y detener el ambiente virtual con el siguiente comando
```bash
deactivate
```

## Adicionales

Cabe mencionar que este repositorio ya cuenta con un proyecto de ejemplo el cual considera las siguientes entidades:

|User||
|--|--|
|id| Identificador único del usuario.|
|name| Nombre del usuario.|
|email| Correo electrónico para acceso.|
|password| Contraseña del usuario.|
|shippingAddress| Dirección principal de envío (opcional hasta que se realice una compra).|

|Category||
|--|--|
|id|Identificador único de la categoría.|
|name|Nombre de la categoría.|
|description|Descripción de la categoría.|

|Product||
|--|--|
|id|Identificador único del producto.|
|name|Nombre del producto.|
|description|Descripción breve del producto.|
|price|Precio del producto.|
|stock|Cantidad disponible del producto.|
|imageUrl|URL de la imagen del producto.|
|categoryId|Identificador de la categoría a la que pertenece el producto.|

|Purchase||
|--|--|
|id|Identificador único de la compra.|
|userId|Identificador del usuario que realiza la compra.|
|products|Lista de id´s de los productos comprados.|
|total|Total pagado.|
|shippingAddress|Dirección de envío utilizada para esta compra.|

## Documentación adicional:

- [Generación de un proyecto adicional](documentacion/GENERAR_PROYECTO.MD)
- [Crear un modelo](documentacion/CREAR_MODELOS.MD)
- [Implementar operaciones CRUD sobre el modelo creado](documentacion/IMPLEMENTAR_CRUD.MD)

**Notas**

- Asegúrate de tener todos los requisitos mínimos instalados antes de comenzar.
- Es recomendable trabajar dentro de un entorno virtual para evitar conflictos con otras dependencias de Python.
- Consulta la documentación oficial de Django para más información y guías avanzadas: [Documentación de Django](https://docs.djangoproject.com/).

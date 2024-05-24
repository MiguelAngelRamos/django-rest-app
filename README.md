## Bienvenidos al proyecto de Django Rest, para una app de ecommerce

1. Para instalar las dependencias de este proyecto porfavor escriba el siguiente comando:

```sh
pip install -r requirements.txt
```

```sh
pip install djangorestframework-simplejwt
```

Nota: recuerda que antes debes tener activado el entorno virtual


# Documentacion Swagger
1. Instala la dependencia
```sh
pip install drf-yasg
```
2. Instala la dependencia en settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'productos'
]
```

3. Debes configurar los staticos en settings.py 
```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
  STATIC_URL = 'static/'
  STATIC_ROOT = BASE_DIR / 'static'
```
4. Las rutas 

```python
from django.contrib import admin
from django.urls import path, include
from productos.api.router import router_post
from productos.views import HelloWorld
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación API REST Django",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_post.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    
]

```

Comienza a generar los estaticos para la documentación

```sh
python manage.py collectstatic
```
Si marca error es probable que necesitas actualizar el setuptools

```sh
pip install --upgrade setuptools
```


## Para poder integrar una tecnologia de Frontend

```sh
 pip install django-cors-headers
```
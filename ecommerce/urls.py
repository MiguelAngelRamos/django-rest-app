
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
#    permission_classes=(permissions.AllowAny,),
)
# from productos.api.views import ProductoListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_post.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('api/productos/', ProductoListView.as_view(), name  = "productos")
    # path('', HelloWorld.as_view(), name="hello")
    
]

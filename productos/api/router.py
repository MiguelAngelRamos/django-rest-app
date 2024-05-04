from rest_framework.routers import DefaultRouter
# from productos.api.views import ProductViewSet
from productos.api.views import ProductModelViewSet

router_post = DefaultRouter()

router_post.register(prefix='productos', viewset=ProductModelViewSet, basename='productos')
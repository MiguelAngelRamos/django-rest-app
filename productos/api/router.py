from rest_framework.routers import DefaultRouter
from productos.api.views import ProductViewSet

router_post = DefaultRouter()

router_post.register(prefix='productos', viewset=ProductViewSet, basename='productos')
from rest_framework.serializers import ModelSerializer
from productos.models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'image', 'precio', 'stock', 'categoria']
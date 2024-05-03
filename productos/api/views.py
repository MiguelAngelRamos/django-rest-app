from rest_framework import status
from rest_framework.views import APIView
from productos.models import Producto
from rest_framework.response import Response
class ProductoListView(APIView):
    
    def get(self, request):
        productos = [producto.nombre for producto in Producto.objects.all()]
        return Response(status=status.HTTP_200_OK, data=productos)
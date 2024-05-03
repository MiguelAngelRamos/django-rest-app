from rest_framework import status
from rest_framework.views import APIView
from productos.models import Producto
from rest_framework.response import Response
from productos.api.serializers import ProductoSerializer

class ProductoListView(APIView):
    
    def get(self, request):
        # productos = [producto.nombre for producto in Producto.objects.all()]
        serializer = ProductoSerializer(Producto.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
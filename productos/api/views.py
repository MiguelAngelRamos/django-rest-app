from rest_framework import status
from rest_framework.views import APIView
from productos.models import Producto
from rest_framework.response import Response
from productos.api.serializers import ProductoSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet


class ProductModelViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset  = Producto.objects.all()
    
# class ProductViewSet(ViewSet):
#     def list(self, request):
#         serializer = ProductoSerializer(Producto.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    
#     def create(self, request):
#         serializer = ProductoSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
    
#     def retrieve(self, request, pk:int):
#         producto = ProductoSerializer(Producto.objects.get(id=pk))
#         return Response(status=status.HTTP_200_OK, data=producto.data)
    
#     def update(self, request, pk:int):
#         producto = Producto.objects.get(pk=pk) # el producto que esta en base de datos
#         serializer = ProductoSerializer(producto, data=request.data) # y en el data=request.data viene los datos que deseo actualizar
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_200_OK, data=serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk:int):
#         producto = Producto.objects.get(pk=pk)
#         producto.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class ProductoListView(APIView):
        
    
#     def get(self, request):
#         # productos = [producto.nombre for producto in Producto.objects.all()]
#         serializer = ProductoSerializer(Producto.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    
#     def post(self, request):
#         serializer = ProductoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
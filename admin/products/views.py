
from rest_framework import viewsets , status
from .models import Products,User
from rest_framework.response import Response
from .Serializer import ProductSerializer
from rest_framework.views import APIView
import random
class ProductViewSets(viewsets.ViewSet):
    def list(self , request): #api/products
        products  = Products.objects.all()
        serializer = ProductSerializer( products , many = True)
        return Response(serializer.data)

    def create(self, request): #api/products
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data , status = status.HTTP_201_CREATED)

    def retrieve(self, request ,pk = None ):
        product  = Products.objects.get(id = pk )  
        serializer = ProductSerializer(product , many = False)
        return Response(serializer.data)

    
    def update(self, request ,pk = None ):
        Product = Products.objects.get(id = pk)
        serializer  = serializer(instance = Product , data = request.data) 
        serializer.is_valid(raise_exception = True)
        return Response(serializer.data , status = status.HTTP_202_ACCEPTED)

    def distory(self, request ,pk = None ):
        Product = Products.objects.get(id = pk)
        Product.delete() 
        return Response(status.HTTP_204_NO_CONTENT)



class UserAPIView(APIView):
    def get(self , request):
            users = User.objects.all()
            user  = random.choice(users)
            return Response({
                'id' : user.id
            })

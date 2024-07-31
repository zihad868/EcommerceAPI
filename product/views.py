from rest_framework import generics
from rest_framework import permissions
from django.views.generic import TemplateView

from . models import (
    Product, 
    Category
)

from . serializers import (
    ProductSerializer,
    CategorySerializer,
    RetrieveProductSerializer,
    RetrieveCategorySerializer
)


class Home(TemplateView):
    template_name = 'Home/Home.html'


# Category List
class ListCategory(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProduct(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.order_by('-id')
    
    

class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = RetrieveProductSerializer
    lookup_field = 'slug'


class RetrieveCategory(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = RetrieveCategorySerializer
    lookup_field = 'slug'
    

# Create Product
class CreateProduct(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Update Product
class UpdateProduct(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    

# Destroy Product
class DestroyProduct(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    
    
# Category API
class CreateCategory(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
# Update Category
class UpdateCategory(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    

# Destroy Category
class DestroyCategory(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
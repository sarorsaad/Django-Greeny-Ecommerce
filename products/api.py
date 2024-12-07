# view api 

from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.decorators import api_view 
from .serializers import ProductSerializer ,ProductDetailSerializer, BrandListSerializer ,BrandDetailSerializer, CategorySerializer , CategoryDetailSerializer
from .models import Brand, Product , Category
from rest_framework.permissions import IsAuthenticated
from .pagination import MyPagination
import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter



class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','subtitle','price']
    filterset_class = ProductFilter
    search_fields = ['name', 'subtitle']
    # permission_classes = [IsAuthenticated]
    
    
class ProductDetailAPI(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()    

    
class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()        
    
    
class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    

    
class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()           
    
    
    
    
    
'''
# products : 
    - list brands
    - detail  category 
    - list categories 
    - detail category
'''

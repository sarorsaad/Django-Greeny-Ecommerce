# form like file 
from rest_framework import serializers
from .models import Product , Category , Brand , ProductReview
import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
   
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ['id','name','sku','subtitle','desc','flag','price','image','quantity','video_url','category','brand']
   
    
class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand',many=True)
    class Meta:
        model = Brand
        fields = ['id','name','image','products']
        
        
        
class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source='product_category',many=True)
    class Meta:
        model = Category
        fields = ['id','name','image','products']
        


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['user','product','rate','review']
        

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ProductReviewSerializer(source='product_review',many=True)
    class Meta :
        model = Product
        fields = ['id','name','sku','subtitle','desc','flag','price','image','quantity','video_url','category','brand','reviews']
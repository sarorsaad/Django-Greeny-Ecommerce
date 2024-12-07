from django.urls import path
from .views import ProductList , ProductDetail , BrandList , BrandDetail , CategoryList , post_list,add_review

from .api import ProductListAPI ,ProductDetailAPI , BrandListAPI , BrandDetailAPI , CategoryDetailAPI , CategoryListAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name='products'

urlpatterns = [
    path('testing/' , post_list),
    path('' , ProductList.as_view() , name='product_list'),
    path('<int:pk>' , ProductDetail.as_view() , name='product_details'),
    path('<int:id>/add-review' , add_review , name='add_review'),
    path('brands/' , BrandList.as_view() , name='brand_list'),
    path('brands/<int:pk>' , BrandDetail.as_view() , name='brand_detail'),
    path('category/' , CategoryList.as_view() , name='category_list'),
    
    


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        
    path('api/' , ProductListAPI.as_view()),
    path('api/<int:pk>' , ProductDetailAPI.as_view()),
    path('api/brands' , BrandListAPI.as_view()),
    path('api/brands/<int:pk>' , BrandDetailAPI.as_view()),
    path('api/category' , CategoryListAPI.as_view()),
    path('api/category/<int:pk>' , CategoryDetailAPI.as_view()),
]


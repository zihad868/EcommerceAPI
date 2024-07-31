from django.urls import path
from . views import (
    Home,
    ListProduct,
    ListCategory,
    RetrieveProduct,
    RetrieveCategory,
    
    # Product
    CreateProduct,
    UpdateProduct,
    DestroyProduct,
    
    # Category
    CreateCategory,
    UpdateCategory,
    DestroyCategory
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    
    path('list-product/', ListProduct.as_view(), name='list-product'),
    path('list-category/', ListCategory.as_view(), name='list-category'),
    path('retrieve-product/<str:slug>/', RetrieveProduct.as_view(), name='retrieve-product'),
    path('retrieve-category/<str:slug>/', RetrieveCategory.as_view(), name='retrieve-category'),
    
    # Product Create Update Delete API
    path('create-product/', CreateProduct.as_view(), name='create-product'),
    path('update-product/<int:id>/', UpdateProduct.as_view(), name='update-product'),
    path('destroy-product/<int:id>/', DestroyProduct.as_view(), name='destroy-product'),
    
    # Category Create Update Delete API
    path('create-category/', CreateCategory.as_view(), name='create-category'),
    path('update-category/<int:id>/', UpdateCategory.as_view(), name='update-category'),
    path('destroy-category/<int:id>/', DestroyCategory.as_view(), name='destroy-category'),
]
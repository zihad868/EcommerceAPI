from django.urls import path
from . views import (
    ListProduct,
    ListCategory,
    RetrieveProduct,
    RetrieveCategory,
    CreateProduct
)

urlpatterns = [
    path('list-product/', ListProduct.as_view(), name='list-product'),
    path('list-category/', ListCategory.as_view(), name='list-category'),
    path('retrieve-product/<str:slug>/', RetrieveProduct.as_view(), name='retrieve-product'),
    path('retrieve-category/<str:slug>/', RetrieveCategory.as_view(), name='retrieve-category'),
    
    # CRUD API
    path('create-product/', CreateProduct.as_view(), name='create-product'),
]
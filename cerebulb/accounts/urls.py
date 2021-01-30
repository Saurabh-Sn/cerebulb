from django.urls import path, re_path, include
from rest_framework import routers
from .api import CategoryView, ProductView
from .views import  USerLoginView,products,add_product, edit_product
router = routers.DefaultRouter()
router.register('category', CategoryView, 'category')
router.register('product', ProductView, 'product')


urlpatterns = [

    path('api/v1/', include(router.urls)),
    path('login/', USerLoginView.as_view(), name='login_page'),
    path('products/', products, name='product_list'),
    path('add/product', add_product, name='add_product'),
    path('edit_product/<int:pk>/', edit_product, name='edit_product'),
]
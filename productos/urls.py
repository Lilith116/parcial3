from django.urls import path
from . import views
from productos.views import agregar_producto,eliminar_producto,restar_producto,limpiar_carrito
from .views import tienda, shopping_cart, registro



urlpatterns = [
    path('index', views.index, name='index'),
    path('About', views.About, name='About'),
    path('Adopciones', views.Adopciones, name='Adopciones'),
    path('tienda', views.tienda, name='tienda'),
    path('ShoppingCart', views.ShoppingCart, name='ShoppingCart'),
    path('crud', views.crud, name='crud'),
    path('clientes_add', views.clientes_add, name='clientes_add'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientes_Update', views.clientes_Update, name='clientes_Update'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('', tienda, name='productos'),
    path('carrito/', shopping_cart, name='shopping_cart'),
    path('registro/', registro, name="registro"),
    





    
    
]

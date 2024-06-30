from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('About', views.About, name='About'),
    path('Adopciones', views.Adopciones, name='Adopciones'),
    path('Productos', views.Productos, name='Productos'),
    path('ShoppingCart', views.ShoppingCart, name='ShoppingCart'),
    path('crud', views.crud, name='crud'),
    path('clientesadd', views.clientesadd, name='clientesadd'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', views.clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', views.clientesUpdate, name='clientesUpdate'),
    path('agregar_al_carro/<int:producto_id/', views.agregar_al_carro, name='agregar_al_carro'),
    path('quitar_del_carro/int:item_producto_id>/', views.quitar_del_carro, name='quitar_del_carro' ),
    path('lista_productos/', views.lista_productos, name='lista_productos'),





    
    
]

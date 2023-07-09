from django.urls import path
from . import views
from .views import login_view
from django.contrib.auth.views import LogoutView




urlpatterns =[
    path('',views.cargarIndex),
    path('index',views.cargarIndex),
    path('about',views.cargarAbout),
    path('colabora',views.cargarColabora),
    path('contactanos',views.cargarContactanos),
    path('equipo',views.cargarEquipo),
    path('registro',views.cargarAgregarUsuario,name='registro'),
    path('registroUsu',views.agregarUsuario),
    path('mi_cuenta/<str:id>', views.cargarEditarUsuario, name='mi_cuenta'),
    path('editarUsuario',views.editarUsuario),
    path('agregarProductos',views.cargarAgregarProducto),
    path('agregarProd',views.agregarProductos),
    path('editarProducto/<id>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProductos/<id>',views.eliminarProductos),
    path('success',views.cargarSuccess),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/index'), name='logout'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('agregar/<int:id_producto>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:id_producto>/', views.eliminar_producto, name="Del"),
    path('restar/<int:id_producto>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
    
    
]

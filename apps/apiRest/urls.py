from django.urls import path
from . import views


urlpatterns = [
  path('listadoProductos',views.ObtenerProductosApi.as_view())
]
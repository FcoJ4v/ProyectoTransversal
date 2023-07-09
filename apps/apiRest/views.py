from django.shortcuts import render

from django.views import View
from apps.webHuertita.models import Producto
from django.http import JsonResponse
# Create your views here.


class ObtenerProductosApi(View):
    def get(self,request):
        prods = Producto.objects.all()
        return JsonResponse(list(prods.values()),safe=False)
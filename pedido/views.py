from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class PagarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar Pedido')

class FecharPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('FecharPedido')

class DetalhePedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('DetalhePedido')

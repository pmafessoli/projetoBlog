from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

class CriarPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Criar')

class  UpdatePerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update')

class LoginPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class LogoutPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
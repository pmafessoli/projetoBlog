from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from . import forms


class BasePerfil(View):
    template_name = 'perfil/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user, 
                    instance=self.request.user,
                ),
                
                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                     data=self.request.POST or None
                ),

                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }


        self.renderizar = render(
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar


class CriarPerfil(BasePerfil):
    def post(self, *args, **kwargs):
        return self.renderizar

class  UpdatePerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Update')

class LoginPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')

class LogoutPerfil(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
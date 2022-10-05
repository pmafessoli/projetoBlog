from django.urls import path
from . import views

app_name= 'perfil'

urlpatterns = [
    path('', views.CriarPerfil.as_view(), name='criar'),
    path('update/', views.UpdatePerfil.as_view(), name='update'),
    path('login/', views.LoginPerfil.as_view(), name='login'),
    path('logout/', views.LogoutPerfil.as_view(), name='logout'),
]

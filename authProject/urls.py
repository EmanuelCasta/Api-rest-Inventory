"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authApp.views.UsuarioCreateView import UsuarioCreateView
from authApp.views.UsuarioDetailView import UsuarioDetailView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [

    #Crear Usuario
    path('usuario/',views.UsuarioCreateView.as_view()),
    #Crear Proveedor
    #path('proveedor/',views.ProveedorCreateView.as_view()),
    #Crear categoria
    #path('categoria/',views.CategoriaCreateView.as_view()),
    #Mostrar todas las empresas
    #path('empresa/all/',views.EmpresaDetailView.as_view()),
    # Ingresar al sistema
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),


    # =======Los que necesitan auth============ 
    # pk es el id del Usuario 
    # pkProducto es el id del producto
    path('producto/<int:pk>/',views.ProductoCreateView.as_view()),
    path('producto/all/<int:pk>/',views.ProductoAllView.as_view()),
    path('producto/<int:pk>&<int:pkProducto>/',views.ProductoDetailView.as_view()),
    #path('proveedor/<int:pk>/',views.ProveedorDetailView.as_view()),
    #path('categoria/<int:pk>/',views.CategoriaDetailView.as_view()),
    path('usuario/<int:pk>/',views.UsuarioDetailView.as_view()),


    #         """Administrador es el que asigna las empresas"""
    #path('empresa/',views.EmpresaCreateView.as_view()),

]

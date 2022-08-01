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
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/',views.ProductoCreateView.as_view()),
    path('producto/all/',views.ProductoAllView.as_view()),
    path('producto/<int:pk>/',views.ProductoDetailView.as_view()),
    path('proveedor/',views.ProveedorCreateView.as_view()),
    path('proveedor/<int:pk>/',views.ProveedorDetailView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('empresa/',views.EmpresaCreateView.as_view()),
    path('empresa/<int:pk>/',views.EmpresaDetailView.as_view())
]

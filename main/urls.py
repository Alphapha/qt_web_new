"""main应用URL配置"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
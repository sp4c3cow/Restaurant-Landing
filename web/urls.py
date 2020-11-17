from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.reserve_table, name='reservation')
]


from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('pessoas/', views.pessoasview),
    path('db1', views.db1),
    path('db2', views.db2),
    path('thanks/', views.thanks)
]
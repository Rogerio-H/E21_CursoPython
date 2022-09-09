from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('pessoas_list/', views.pessoas_list),
    path('pessoa_add', views.pessoa_add),
    path('pessoa_edit/<int:id>', views.pessoa_edit, name="edit-pessoa"),
    path('pessoa_delete/<int:id>', views.pessoa_delete, name="delete-pessoa"),
    # path('db1', views.db1),
    # path('db2', views.db2),
    # path('thanks/', views.thanks)
]
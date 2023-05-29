from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crear_tarea/', views.crear_tarea, name="crear-tarea"),
    path('crear_responsable/', views.crear_responsable, name ="crear-responsable"),
    path('crear_local/', views.crear_local, name = "crear-local"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base.html'),
    path('medicos/', views.listar_medicos, name='listar_medicos.html'),
    path('consultas/', views.detalhes_consulta, name='exibir_consulta.html'),
    path('consultas/nova/', views.criar_consulta, name='form_consulta.html'),
    path('consultas/<int:pk>/', views.detalhe_consulta, name='visualizar_consulta.html')

]
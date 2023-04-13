from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('total_vendido', views.total_vendido, name='total_vendido'),
    path('relatorio_faturamento', views.relatorio_faturamento, name='relatorio_faturamento'),
    path('relatorio_produtos', views.relatorio_produtos, name='relatorio_produtos'),
    path('relatorio_funcionario', views.relatorio_funcionario, name='relatorio_funcionario'),
    path('relatorio_despesas', views.relatorio_despesas, name='relatorio_despesas'),
    path('despesa_anual', views.despesa_anual, name='despesa_anual'),
    path('lucro_liquido', views.lucro_liquido, name='lucro_liquido')
]
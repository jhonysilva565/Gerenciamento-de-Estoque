from django.urls import path
from gerencia_plus import views



urlpatterns = [
    path('', views.home, name='home'),
    path('inicial/', views.inicial, name='inicial'),
    path('salvo/', views.salvo, name='salvo'),
    path('compra/', views.compra, name='compra'),
    path('avaliar/', views.avaliar, name='avaliar'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('contato/', views.contato, name='contato'),
    path('emailsucesso/', views.emailsucesso, name='emailsucesso'),
    path('tutorial/', views.turorial, name='tutorial'),
    path('api/estoque/<int:pk>/', views.EstoqueDeleteView.as_view(), name='estoque_delete'),
    path('enviar-formulario', views.enviar_formulario, name='enviar_formulario'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
]


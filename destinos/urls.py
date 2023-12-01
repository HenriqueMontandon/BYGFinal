from django.urls import path
from . import views

app_name = 'destinos'
urlpatterns = [
    path('', views.DestinoListView.as_view(), name='index'), 
    path('search/', views.search_destinos, name='search'),
    path('create/', views.create_destino, name='create'),
    path('lists/', views.ListListView.as_view(), name='lists'),
    path('lists/create', views.ListCreateView.as_view(), name='create-list'),
    path('<int:destino_id>/', views.detail_destino, name='detail'),
    path('lists/<int:pk>/', views.RoteiroDetailView, name='roteiro'),
    path('lists/update/<int:pk>/', views.update_Roteiro.as_view(), name="update"),
    path('lists/delete/<int:pk>', views.delete_Roteiro.as_view(), name ='delete'),
    path('listar_preferencias_tipo/', views.listar_preferencias_tipo, name='listar_preferencias_tipo'),
    path('add_preferencias_tipo/', views.add_preferencias_tipo, name='add_preferencias_tipo'),
    path('delete_preferencias_tipo/', views.delete_preferencias_tipo, name='delete_preferencias_tipo'),
    path('meu_perfil/', views.meu_perfil, name='meu_perfil'),
    path('remover_preferencia/<int:preferencia_id>/', views.remover_preferencia, name='remover_preferencia'),
    path('lists/<int:pk>/addEvento', views.CreateEventoView.as_view(), name ='addEvento'),
    path('createCategory/', views.CreateCategoriaView.as_view(), name='createCategoria'),
    path('listCategorias/', views.listCategorias.as_view(), name='listCategorias'),
    path('categoria/<int:pk>/delete', views.deleteCategoriaView.as_view(), name='deleteCategoria'),
    path('<int:pk>/add_atracao_caracteristica/', views.add_atracao_caracteristica, name='add_atracao_caracteristica'),
    path('remover_atracao_caracteristica/<int:caracteristica_id>/', views.remover_atracao_caracteristica, name='remover_atracao_caracteristica'),
    path('get_all', views.getDestinos),
    path('post/',views.postDestino),
    path('put/<int:pk>/', views.updateDestino),
    path('delete/<int:pk>/', views.deleteDestino),
]
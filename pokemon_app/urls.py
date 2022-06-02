from django.urls import path
from . import views

urlpatterns =[
    path('', views.Home.as_view(), name='home'),
    path('pokemon/', views.PokemonList.as_view(), name='pokemon'),
    path('pokemon/new/', views.PokemonCreate.as_view(), name='pokemon_create'),
    path('pokemon/<int:pk>/', views.PokemonDetail.as_view(), name='pokemon_detail'),
    path('pokemon/<int:pk>/update', views.PokemonUpdate.as_view(), name='pokemon_update'),
    path('pokemon/<int:pk>/delete', views.PokemonDelete.as_view(), name='pokemon_delete'),
    path('pokemon/<int:pk>/moves/new', views.MoveCreate.as_view(), name='move_create'),
    path('groups/<int:pk>/pokemons/<int:pokemon_pk>/', views.GroupPokemonAssoc.as_view(), name ='group_pokemon_assoc'),
]
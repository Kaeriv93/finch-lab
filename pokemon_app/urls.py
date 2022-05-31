from django.urls import path
from . import views

urlpatterns =[
    path('', views.Home.as_view(), name='home'),
    path('pokemon/', views.PokemonList.as_view(), name='pokemon'),
    path('pokemon/new/', views.PokemonCreate.as_view(), name='pokemon_create'),
    path('/pokemon/<int:pk>/', views.PokemonDetail.as_view(), name='pokemon_detail')
]
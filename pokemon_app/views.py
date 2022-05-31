from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from .models import Pokemon

class Home(TemplateView):
    template_name = 'home.html'
    
class PokemonList(TemplateView):
    template_name = 'pokemon.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemons'] = Pokemon.objects.all()
        return context

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'sprite', 'index', 'bio', 'can_evolve']
    template_name = 'pokemon_create.html'
    success_url = '/pokemon/'

class PokemonDetail(DetailView):
    model = Pokemon
    template_name = 'pokemon_detail.html' 

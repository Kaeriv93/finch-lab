from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Pokemon
from django.urls import reverse

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
    
class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'sprite', 'index', 'bio', 'can_evolve']
    template_name = 'pokemon_update.html'
    
    def get_success_url(self):
        return reverse('pokemon_detail', kwargs={'pk': self.object.pk})

class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = 'pokemon_delete_confirmation.html'
    success_url = '/pokemon/'
from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Pokemon, Move, Group, Comment
from django.urls import reverse

class Home(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context
    
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
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['groups']= Group.objects.all()
        return context
    
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
    
class MoveCreate(View):
    def post(self,request, pk):
        name = request.POST.get('name')
        type = request.POST.get('type')
        power = request.POST.get('power')
        pokemon = Pokemon.objects.get(pk=pk)
        Move.objects.create(name = name, type = type, power = power, pokemon = pokemon)
        return redirect('pokemon_detail', pk=pk)
        
class GroupCreate(CreateView):
    model = Group
    fields = ['name']
    template_name ='group_create.html'
    success_url = '/pokemon/'


# class PokemonCreate(CreateView):
#     model = Pokemon
#     fields = ['name', 'sprite', 'index', 'bio', 'can_evolve']
#     template_name = 'pokemon_create.html'
#     success_url = '/pokemon/'


class GroupPokemonAssoc(View):
    def get(self,request,pk,pokemon_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Group.objects.get(pk=pk).pokemons.remove(pokemon_pk)
        if assoc == "add":
            Group.objects.get(pk=pk).pokemons.add(pokemon_pk)
        return redirect('home')
    

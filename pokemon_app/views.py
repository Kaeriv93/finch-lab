from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Pokemon, Move, Group
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class Home(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class PokemonList(TemplateView):
    template_name = 'pokemon.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context['pokemons'] = Pokemon.objects.filter(
                name_icontains= name, user=self.request.user)
            context['header'] = f"Searching for {name}"
            
        else:
            context['pokemons'] = Pokemon.objects.filter(user = self.request.user)
            context['header'] ='Pokemon!'
        # context['pokemons'] = Pokemon.objects.all()
        return context

class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'sprite', 'index', 'bio', 'can_evolve']
    template_name = 'pokemon_create.html'
    success_url = '/pokemon/'
    
    def form_valid(self,form):
        print(self.kwargs)
        return reverse('pokemon_detail', kwargs={'pk': self.object.pk})

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


class GroupPokemonAssoc(View):
    def get(self,request,pk,pokemon_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Group.objects.get(pk=pk).pokemons.remove(pokemon_pk)
        if assoc == "add":
            Group.objects.get(pk=pk).pokemons.add(pokemon_pk)
        return redirect('home')
    
class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('pokemon_list')
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
        
# class Signup(View):
#     # show a form to fill out
#     def get(self, request):
#         form = UserCreationForm()
#         context = {"form": form}
#         return render(request, "registration/signup.html", context)
#     # on form ssubmit validate the form and login the user.
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("artist_list")
#         else:
#             context = {"form": form}
#             return render(request, "registration/signup.html", context)

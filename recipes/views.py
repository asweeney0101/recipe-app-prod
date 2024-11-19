from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Recipe
from .forms import RecipesSearchForm

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'recipes/home.html'
      

class RecipesListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes.html'
    context_object_name = 'recipes'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RecipesSearchForm()
        return context
    
    def post(self, request, *args, **kwargs):
        search_query = request.POST.get('search_query')
        recipes = Recipe.objects.filter(
            Q(name__icontains=search_query) | 
            Q(ingredients__icontains=search_query)
        )
        context = {}
        context['form'] = RecipesSearchForm()
        context['recipes'] = recipes
        
        return render(request, self.template_name, context)


class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['name', 'cooking_time', 'ingredients', 'description', 'pic']
    template_name = 'recipes/recipe_form.html'
    success_url = '/recipes/' 


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    
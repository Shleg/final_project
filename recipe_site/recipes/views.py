import logging

from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View

from .models import Recipe, RecipeCategory
from .forms import RecipeForm
import random


def home(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 5))
    return render(request, 'recipes/home.html', {'recipes': random_recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    categories = RecipeCategory.objects.filter(recipe=recipe).select_related('category')
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'categories': categories})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'recipes/login.html'
    success_url = '/'


logger = logging.getLogger(__name__)


class CustomLogoutView(View):
    next_page = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        logger.debug("Выход из системы выполнен")
        return redirect(self.next_page)


def recipe_form(request, recipe_id=None):
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('recipe_detail', recipe_id=recipe.pk)
        else:
            form = RecipeForm(instance=recipe)
    else:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                new_recipe = form.save(commit=False)
                new_recipe.author = request.user
                new_recipe.save()
                return redirect('recipe_detail', recipe_id=new_recipe.pk)
        else:
            form = RecipeForm()

    # Добавьте recipe_id в контекст, даже если он равен None
    return render(request, 'recipes/recipe_form.html', {'form': form, 'recipe_id': recipe_id})

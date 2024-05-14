from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField(default=0)  # Время приготовления в минутах
    image = models.ImageField(upload_to='recipes_images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления рецепта в категорию

    def __str__(self):
        return f"{self.recipe.title} in {self.category.name}"

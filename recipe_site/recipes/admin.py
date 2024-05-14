from django.contrib import admin
from .models import Recipe, Category, RecipeCategory


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time', 'creation_date')
    list_filter = ('cooking_time', 'author')
    search_fields = ('title', 'description', 'ingredients')
    date_hierarchy = 'creation_date'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'category', 'created_at')
    list_filter = ('category',)
    date_hierarchy = 'created_at'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)

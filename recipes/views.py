from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient
from .forms import RecipeForm, IngredientForm

# Список рецептов
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, template_name='recipe_list.html',context={'recipes': recipes})

# Детальная информация о рецепте
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, template_name='recipe_detail.html', context={'recipe': recipe})

# Добавление нового рецепта
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, template_name='add_recipe.html', context={'form': form})

# Добавление ингредиента к рецепту
def add_ingredient(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = IngredientForm()
    return render(request, template_name='add_ingredient.html', context={'form': form, 'recipe': recipe})

# Удаление рецепта
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('recipe_list')


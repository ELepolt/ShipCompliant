from datetime import datetime, date, timedelta
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from website.forms import IngredientForm
from website.models import BeerRecipe, IngredientType, Ingredient, BeerIngredient

# import json
# import pdb

def index(request):
	ingredient_types = IngredientType.objects.all()
	ingredient_dict = OrderedDict()
	ingredient_types = IngredientType.objects.all()
	# import pdb
	# pdb.set_trace()
	for ingredient_type in ingredient_types:
		ingredients = Ingredient.objects.filter(ingredient_type=ingredient_type)
		ingredient_dict[ingredient_type] = ingredients
	
	recipe_list = OrderedDict()
	recipes = BeerRecipe.objects.all()

	for recipe in recipes:
		length = len(recipe.ingredients.split(";")) - 1
		ingredient_list = []
		for x in range(0,length):
			beer_ingredient = BeerIngredient.objects.get(pk=recipe.ingredients.split(";")[x])
			ingredient_list.append(beer_ingredient)

		recipe_list[recipe] = ingredient_list



	context = {
		'ingredient_types': ingredient_types,
		'ingredient_dict': ingredient_dict,
		'recipe_list': recipe_list,
	}
	return render(request, 'website/index.html', context)

def addrecipe(request):
	if request.method == 'POST':
		recipe = BeerRecipe()
		recipe.title = request.POST['name']
		recipe.instructions = request.POST['instructions']
		
		ingredient_list = ""

		ingredients = request.POST['ingredients']
		length = len(ingredients.split(";"))-1
		for x in range(0, length):
			ingredient = BeerIngredient()			
			ingredient.ingredient = Ingredient.objects.get(name = ingredients.split(";")[x].split("-")[0])
			ingredient.amount = ingredients.split(";")[x].split("-")[1]

			ingredient.save()

			ingredient_list += str(ingredient.id) + ";"

		recipe.ingredients = ingredient_list
		recipe.save()

	return redirect('index')

def addingredient(request):
	context = ""
	if request.method == 'POST':
		ingredient_types = IngredientType.objects.all()
		
		context = {
			'ingredient_types': ingredient_types,
		}

		# if not request.user.is_authenticated():
		# 	context['user_form'] = UserForm()
		# else:
		# 	checkins = FanStatsUser.objects.get(user=request.user).checkins.all()
		# 	context['checkins'] = set(map(lambda x: x.sport_type.feed_id, checkins))

		return render(request, 'website/addingredient.html', context)
	else:
		return render(request, 'website/addingredient.html', context)

def addnewingredient(request):
	if request.method == 'POST':
		context = ""
		ingredient = Ingredient()
		
		ingredient_id = request.POST['ingredient_id']
		ingredient_type = IngredientType.objects.get(ingredient_type=ingredient_id)
		ingredient.name = request.POST['title']
		ingredient.ingredient_type = ingredient_type

		ingredient.save()
		
	return redirect('index')





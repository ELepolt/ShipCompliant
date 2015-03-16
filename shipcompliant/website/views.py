from datetime import datetime, date, timedelta
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from website.forms import IngredientForm
from website.models import BeerRecipe, IngredientType, Ingredient, BeerIngredient

import json
import pdb

def index(request):
	# Gets all the types of ingredients from the DB
	ingredient_types = IngredientType.objects.all()
	
	# Creates an empty Ordered Dictionary
	ingredient_dict = OrderedDict()

	# Loops through the ingredient type list and adds a key value pair
	# of Ingredient and List of Ingredients that match that type
	for ingredient_type in ingredient_types:
		ingredients = Ingredient.objects.filter(ingredient_type=ingredient_type)
		ingredient_dict[ingredient_type] = ingredients
	

	recipe_list = OrderedDict()
	recipes = BeerRecipe.objects.all()

	# Loops through the recipes in the DB to add to the empty OrderedDict()
	for recipe in recipes:

		# Recipe ingredients are stored as a semi-colon separated list
		# len() is index 1
		# arrays are index 0
		# length = len(recipe.ingredients.split(";")) - 1
		# ingredient_list = []
		ingredient_list = BeerIngredient.objects.filter(beer_recipe__id = recipe.id)
		# loop from 0 to the length of the ingredient list
		# for x in range(0,length):
		# 	# Get the ingredient that the id matches with
		# 	beer_ingredient = BeerIngredient.objects.get(pk=recipe.ingredients.split(";")[x])
			
		# 	# Add ingredient to the ingredient_list
		# 	ingredient_list.append(beer_ingredient)
			
		# attach the ingredient list to the recipe
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
		recipe.title = request.POST['title']
		recipe.instructions = request.POST['instructions']
		recipe.description = request.POST['description']
		recipe.save()
		
		ingredient_list = ""
		ingredients = request.POST['ingredients']
		amounts = request.POST['amounts']
		length = len(ingredients.split(";"))-1
		for x in range(0, length):
			ingredient = BeerIngredient()
			ingredient.beer_recipe = recipe
			ingredient.ingredient = Ingredient.objects.get(id = ingredients.split(";")[x])
			ingredient.amount = amounts.split(";")[x]

			ingredient.save()


	return redirect('index')

def addnewingredient(request):
	if request.method == 'POST':
		context = ""
		ingredient = Ingredient()
		
		ingredient_type_id = request.POST['ingredient_type_id']
		ingredient_type = IngredientType.objects.get(id=ingredient_type_id)
		ingredient.name = request.POST['ingredient_name']
		ingredient.ingredient_type = ingredient_type
		
		ingredient.save()
		# pdb.set_trace()
		return HttpResponse(str(ingredient.id) + ";" + str(ingredient.name) + ";" + str(ingredient.ingredient_type.display_name))
	return ""





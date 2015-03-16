from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# The instructions and title of the beer
class BeerRecipe(models.Model):
	title = models.CharField(max_length=64)
	description = models.CharField(max_length=64)
	instructions = models.CharField(max_length = 1000)

# General ingredient types like Yeast or Grain or Hops
class IngredientType(models.Model):
	display_name = models.CharField(max_length=16)

# The actual specific names of the ingredient types
class Ingredient(models.Model):
	ingredient_type = models.ForeignKey(IngredientType)
	name = models.CharField(max_length=64, unique=True)

# The amount and type of ingredient and the beer it ties to
class BeerIngredient(models.Model):
	beer_recipe = models.ForeignKey(BeerRecipe)
	ingredient = models.ForeignKey(Ingredient)
	amount = models.CharField(max_length=16)
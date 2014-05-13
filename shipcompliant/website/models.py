from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class BeerRecipe(models.Model):
	title = models.CharField(max_length=64)
	ingredients = models.CharField(max_length=128)
	instructions = models.CharField(max_length = 1000)

class IngredientType(models.Model):
	ingredient_type = models.CharField(max_length=16)
	display_name = models.CharField(max_length=16)
	
class Ingredient(models.Model):
	ingredient_type = models.ForeignKey(IngredientType)
	name = models.CharField(max_length=64, unique=True)

class BeerIngredient(models.Model):
	ingredient = models.ForeignKey(Ingredient)
	amount = models.CharField(max_length=16)
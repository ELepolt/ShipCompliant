from django import forms
from django.contrib.auth.models import User
from website.models import IngredientType, Ingredient

class IngredientForm(forms.Form):
	title = forms.CharField(max_length=64)
	ingredient_id = forms.IntegerField()
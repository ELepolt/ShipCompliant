from django.contrib import admin
from django import forms
from django.forms import Textarea
from django.db import models

from website.models import IngredientType, Ingredient

# Sets the order of fields that appear on admin page
class IngredientTypeAdmin(admin.ModelAdmin):
	fields = ['ingredient_type', 'display_name']
	list_display = ('ingredient_type', 'display_name')

class IngredientAdmin(admin.ModelAdmin):
	fields = ['ingredient_type', 'name']
	list_display = ('ingredient_type', 'name')

admin.site.register(IngredientType, IngredientTypeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
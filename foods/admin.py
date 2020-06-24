from django.contrib import admin

from .models import Food, FoodNutrient


admin.site.register(Food)
admin.site.register(FoodNutrient)

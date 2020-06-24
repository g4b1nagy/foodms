from django.contrib import admin

from .models import Food, FoodNutrient


class FoodNutrientInline(admin.TabularInline):
    model = FoodNutrient
    extra = 1


class FoodAdmin(admin.ModelAdmin):
    inlines = (FoodNutrientInline,)


admin.site.register(Food, FoodAdmin)
admin.site.register(FoodNutrient)

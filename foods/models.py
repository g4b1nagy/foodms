from django.db import models

from nutrients.models import Nutrient


class Food(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)

    # e.g. "Grilled cheese sandwich"
    name = models.CharField(max_length=64, db_index=True)
    description = models.CharField(max_length=1024)
    is_active = models.BooleanField(default=True, db_index=True)
    nutrients = models.ManyToManyField(Nutrient, through='FoodNutrient', through_fields=('food', 'nutrient'))

    def __str__(self):
        return self.name


class FoodNutrient(models.Model):
    # models.CASCADE: Django also deletes the object containing the ForeignKey
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['food', 'nutrient'], name='unique_food_nutrient'),
        ]

    def __str__(self):
        return '{} {}'.format(self.food.name, self.nutrient.name)

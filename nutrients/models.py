from django.db import models


class Measure(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)

    # e.g. unit: "gram", symbol: "g"
    unit = models.CharField(max_length=16, unique=True)
    symbol = models.CharField(max_length=8, unique=True)

    # This should only be needed if we need to support multiple units of measurement
    # for the same quantity i.e. support both "gram" and "kilogram". If this is the case,
    # we should know that they measure they same quantity and, provided the right formulas,
    # may be added together if needed.
    # QUANTITY_CHOICES = [
    #     (CALORIE, 'calorie'),
    #     (WEIGHT, 'weight'),
    #     (VOLUME, 'volume'),
    # ]
    # quantity = models.CharField(max_length=8, choices=QUANTITY_CHOICES)

    def __str__(self):
        return self.unit


class Nutrient(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)

    # e.g. "Calories" or "Protein"
    name = models.CharField(max_length=16, unique=True)

    # models.PROTECT: prevent deletion of the referenced object by raising ProtectedError
    measure = models.ForeignKey(Measure, related_name='nutrients', on_delete=models.PROTECT)

    def __str__(self):
        return '{} ({})'.format(self.name, self.measure.symbol)

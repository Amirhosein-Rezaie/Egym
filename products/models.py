from django.db import models

from django.core.validators import (
    MinValueValidator
)


class Product(models.Model):
    name = models.CharField(
        max_length=255, db_index=True, blank=False, null=False)

    price = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    description = models.TextField(blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name

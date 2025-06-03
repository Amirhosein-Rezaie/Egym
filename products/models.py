from django.db import models

from django.core.validators import (
    MinValueValidator
)


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    price = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_name = 'Product'

    def __str__(self):
        return self.title

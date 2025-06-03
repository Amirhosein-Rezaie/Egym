from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class ROLES(models.TextChoices):
        ADMIN = 'ADMIN'
        USER = 'USER'

    role = models.CharField(choices=ROLES.choices,
                            default=ROLES.ADMIN, max_length=10)

    class Meta:
        db_name = 'User'

    def __str__(self):
        return self.username

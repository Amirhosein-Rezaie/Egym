from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    class ROLES(models.TextChoices):
        ADMIN = 'ADMIN'
        USER = 'USER'

    role = models.CharField(choices=ROLES.choices,
                            default=ROLES.USER, max_length=10)

    phone = models.CharField(max_length=11,unique=True,blank=True,null=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.username

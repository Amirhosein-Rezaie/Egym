from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class CustomUser(AbstractUser):
    class ROLES(models.TextChoices):
        ADMIN = 'ADMIN'
        USER = 'USER'

    role = models.CharField(choices=ROLES.choices,
                            default=ROLES.USER, max_length=10)

    phone = models.CharField(max_length=11, unique=True, blank=True, null=True)

    profile = models.ImageField(blank=True, null=True, upload_to="profiles/")

    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.username


class Exercise(models.Model):
    class days(models.TextChoices):
        SATURDAY = 'SATURDAY'
        SUNDAY = 'SUNDAY'
        MONDAY = 'MONDAY'
        TUESDAY = 'TUESDAY'
        WEDNESDAY = 'WEDNESDAY'
        THURSDAY = 'THURSDAY'

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='exercise_user')

    day = models.CharField(choices=days, max_length=20)

    exercise = models.CharField(max_length=255)

    sets = models.IntegerField(validators=[
        MinValueValidator(1)
    ], default=1)

    repetition = models.IntegerField(validators=[
        MinValueValidator(1)
    ], default=8)

    class Meta:
        db_table = 'Exercise'

    def __str__(self):
        return f"{self.exercise} on {self.day}"

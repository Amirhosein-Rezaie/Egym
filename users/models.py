from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from products.models import Product
from home.helper import Helper

tarck_code_order = Helper.genrate_trackcode('ORD')


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


class Order(models.Model):
    class Status(models.TextChoices):
        WAITING = 'WAITING'
        VALIDATED = 'VALIDATED'
        PREPARING = 'PREPARING'
        READY = 'READY'
        DELIVERED = 'DELIVERED'
        COMPLETED = 'COMPLETED'
        CANCELED = 'CANCELED'

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)

    total = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    status = models.CharField(choices=Status, default=Status.WAITING)

    track_code = models.CharField(
        max_length=255, unique=True, editable=False, default=tarck_code_order)

    def __str__(self):
        return f"{self.user} -> {self.track_code}"


class order_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    quaintity = models.IntegerField(validators=[
        MinValueValidator(0)
    ])

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product} -> {self.order}"

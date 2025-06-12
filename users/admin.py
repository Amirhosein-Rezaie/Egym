from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Exercise)
class ExcersiceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(models.order_detail)
class Order_detailAdmin(admin.ModelAdmin):
    pass
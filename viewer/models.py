from decimal import Decimal

from django.db import models
# from django.db.models import (
#     DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
#     Model, TextField, DecimalField
# )

class StorePlace(models.Model):
    shelf = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.shelf}'


class StoreName(models.Model):
    store_name=models.CharField(max_length=128)

    def __str__(self):
        return f'{self.store_name}'

class MainCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

class SubCategory(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

class SparePart(models.Model):
    order_code_brt = models.CharField(max_length=128, primary_key=True)
    order_code_suppliers = models.CharField(max_length=128, unique=True)
    name_CZ = models.CharField(max_length=128)
    name_EN_DE = models.CharField(max_length=128)
    main_category = models.ForeignKey(MainCategory, on_delete= models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete= models.DO_NOTHING)
    quantity = models.IntegerField(default=0)
    price_CZ = models.DecimalField(max_digits=20,decimal_places=2, default=Decimal('0.00'))
    price_EUR = models.DecimalField(max_digits=20,decimal_places=2, default=Decimal('0.00'))
    store_place = models.ForeignKey(StorePlace, on_delete = models.DO_NOTHING)
    store_name = models.ForeignKey(StoreName, on_delete= models.DO_NOTHING)
    description = models.CharField(max_length=256, blank=True, help_text='Example: you can write down the type of machine for SP')

    def __str__(self):
        return f'{self.order_code_brt} {self.name_CZ} {self.quantity}pcs'



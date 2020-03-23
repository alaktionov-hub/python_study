# We will need it for create_at filds . And any others work with data and time
import datetime

from django.db import models  # Basis Django import for models
# We need rewrite basis AbstractUser
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):  # Take abstract user us basis
    def __srt__(self):
        # self wil always return username for Customer
        return "{}".format(self.username)

    wallet = models.PositiveIntegerField(default=1000)

    def from_wallet(self, payment):  # charge for a product
        self.wallet -= payment  # take data from payment
        return self.save()  # save

    def to_wallet(self, return_money):  # UNcharge for a product
        self.wallet += return_money  # return money (need for admin UNcharge)
        return self.save()  # save


class Product(models.Model):  # Take base model
    picture = models.ImageField(max_length=300, blank=True, null=True)  # Save photo # python -m pip install Pillow
    title = models.CharField(max_length=20, unique=True)
    text = models.CharField(max_length=100, null=True, blank=True)  # Describe
    price = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def minus_prod(self, amount):
        self.quantity -= amount
        return self.save()

    def plus_prod(self, amount):
        self.quantity += amount
        return self.save()


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)  # FGK to our customer
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, default=object)  # FGK to our product
    cnt = models.PositiveSmallIntegerField(default=0, blank=True, null=True)  # Count of product
    create_at = models.DateTimeField(auto_now_add=True)  # Need to know when we create purchase to allow UNcharge
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    to_return = models.BooleanField(default=False, blank=True, null=True)  # Special to know about stats return
    returned = models.BooleanField(default=False, blank=True, null=True)  # If was returned

    @property
    def check_cnt_available(self):
        return self.product.quantity >= self.cnt

    @property
    def money_not_enough(self):
        return self.customer.wallet < self.cnt*self.product.price

    def is_returnable(self):
        return True
        #return datetime.timedelta(minutes=3) > timezone.now() - self.create_at
        # Check for possibility for return if still not pass more than 3 min

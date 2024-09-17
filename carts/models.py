from django.db import models

from goods.models import Products
from users.models import User


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def products_price(self):
        return round(self.product.display_price_with_discount() * self.quantity, 2)
        


    def __str__(self):
        return f'Cart {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
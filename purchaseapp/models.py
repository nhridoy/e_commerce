from django.db import models
from userapp.models import User
from productapp.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart_user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.IntegerField(default=1)
    is_purchased = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.product_name}'

    def get_total(self):
        return float(self.quantity * self.product.product_new_price)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    cart = models.ManyToManyField(Cart, related_name='order_cart')
    is_ordered = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=264, blank=True, null=True)
    order_id = models.CharField(max_length=264, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.user_profile.full_name}s order {self.pk}'

    def get_totals(self):
        total = 0
        print(self.cart.all())
        for item in self.cart.all():
            total += float(total+item.get_total())
        return total

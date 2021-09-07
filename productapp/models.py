from django.db import models
from ecomapp.models import Category, SubCategory, Company
import uuid
from multiselectfield import MultiSelectField

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
def image_dir(self, filepath):
    return f'product/{self.product.product_name}/{"product_name.jpg"}'


def default_profile_image():
    return f"image.png"


class Colors(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name_plural = 'Colors'


class Sizes(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name_plural = 'Sizes'


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    subcategory_name = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='product_subcategory')
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='product_company')
    product_name = models.CharField(max_length=264, blank=False, verbose_name='Product Name')
    product_quantity = models.IntegerField(blank=False, verbose_name='Quantity')
    product_price = models.IntegerField(blank=False, verbose_name='Price')
    product_discount = models.IntegerField(blank=False, verbose_name='Discount', help_text='%')
    product_new_price = models.IntegerField(verbose_name='New Price', help_text='Warning: Do not edit this field!!!',
                                            blank=True)
    product_description = models.TextField(verbose_name='Description', blank=False)
    MY_CHOICES = (('red', 'Red'),
                  ('blue', 'Blue'),
                  ('green', 'Green'),
                  ('yellow', 'Yellow'),
                  ('purple', 'Purple'))
    product_colors = models.ManyToManyField(Colors, verbose_name='Available Colors', blank=True)
    product_sizes = models.ManyToManyField(Sizes, verbose_name='Available Sizes', blank=True)

    product_slug = models.SlugField(blank=True)

    # product_images = models.ImageField(blank=False, null=False)

    def save(self, *args, **kwargs):
        self.product_new_price = self.product_price - (self.product_price * self.product_discount) / 100
        self.product_slug = f"{self.product_name.replace(' ','-')}-{self.category_name.category_name.replace(' ','-')}-{self.subcategory_name.subcategory_name.replace(' ','-')}-{self.company_name.company_name.replace(' ','-')}-{uuid.uuid4()}"
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product')
    product_image = models.ImageField(upload_to=image_dir, verbose_name='Product Images')

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Product Images'


class Coupon(models.Model):
    coupon_code = models.CharField(max_length=15, verbose_name='Coupon Code', unique=True)
    discount_amount = models.IntegerField(verbose_name='Discounted Amount')
    is_active = models.BooleanField(verbose_name='Activate Coupon')

    def __str__(self):
        return self.coupon_code

# if not ProductImages:
#     @receiver(post_save, sender=Product)
#     def create_image(sender, instance, created, **kwargs):
#         if created:
#             ProductImages.objects.create(product=instance)

# @receiver(post_save, sender=Product)
# def save_image(sender, instance, **kwargs):
#     instance.image_product.save()

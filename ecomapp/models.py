from django.db import models
from django_resized import ResizedImageField


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30, blank=False, unique=True)

    def __str__(self):
        return self.category_name

    def has_subcategories(self):
        return self.category.count()

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    subcategory_name = models.CharField(max_length=45, blank=False)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name_plural = 'Sub-Categories'


def image_directory(self, filepath):
    return f'company/{self.company_name}/{"company_logo.png"}'


class Company(models.Model):
    company_name = models.CharField(max_length=50, blank=False, unique=True)
    company_logo = ResizedImageField(upload_to=image_directory, blank=False, help_text='Size Recommended: 256x256', size=[256, 256], quality=100)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Companies"



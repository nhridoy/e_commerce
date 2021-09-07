from django.contrib import admin
from ecomapp import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.SubCategory)
admin.site.register(models.Company)

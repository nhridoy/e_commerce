from django.contrib import admin
from adminpanelapp import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.BillingAddress)
admin.site.register(models.ShippingAddress)

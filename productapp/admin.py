from django.contrib import admin
from productapp.models import Product, Colors, Sizes, ProductImages, Coupon, Rating
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('product_description',)


class CustomProductImageAdmin(admin.StackedInline):
    model = ProductImages


class ProductCustomAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    search_fields = ('product_name', 'company_name', 'category_name', 'subcategory_name',)
    list_display = ('product_name', 'company_name', 'category_name', 'subcategory_name', 'product_quantity',)
    list_filter = ('product_name', 'company_name', 'category_name', 'subcategory_name',)
    fieldsets = (
        ("Product Category", {'fields': (('category_name', 'subcategory_name'),), 'classes': ('collapse',)}),
        ('Product Descriptions', {'fields': (('product_name', 'company_name'), (
            'product_quantity', 'product_price', 'product_discount', 'product_new_price'), 'product_description',)}),
        ('Available Options', {'fields': ('product_colors', 'product_sizes',)}),
        ('Others', {'fields': ('product_sales', 'image')})
    )
    readonly_fields = ('product_new_price',)
    summernote_fields = ('product_description',)
    inlines = [CustomProductImageAdmin]


admin.site.register(Colors)
admin.site.register(Sizes)
admin.site.register(Coupon)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(Product, ProductCustomAdmin)

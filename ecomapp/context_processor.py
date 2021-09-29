from ecomapp.models import Category, SubCategory


def menu(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return {
        'categories': categories,
        'subcategories': subcategories,
    }

from ecomapp.models import Category, SubCategory
from productapp.models import WishList


def menu(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return {
        'categories': categories,
        'subcategories': subcategories,
    }


def count(request):
    if request.user.is_authenticated:
        wishlist_count = WishList.objects.filter(user=request.user).count()
        return {
            'wishlist_count': wishlist_count,
        }
    return {
        'hello': 'hello'
    }

from django.shortcuts import render
from productapp.models import Company, Category, SubCategory, Product, ProductImages, Colors, Sizes


# Create your views here.

def indexView(request):
    companies = Company.objects.all()
    electronics = Product.objects.filter(category_name__category_name='Electronic Devices').order_by('-added_date')[:10]
    new_products = Product.objects.all().order_by('-added_date')[:10]
    top_selling = Product.objects.all().order_by('-total_order')[:10]
    product_images = ProductImages.objects.all()

    context = {
        'companies': companies,
        'electronics': electronics,
        'product_images': product_images,
        'new_products': new_products,
        'top_selling': top_selling,
    }
    return render(request, 'home/index.html', context)


def pageView(request, category):
    products = Product.objects.all()
    colors = Colors.objects.all()
    sizes = Sizes.objects.all()
    context = {
        'products': products,
        'colors': colors,
        'sizes': sizes,
        'path': str(request.path).split('/')[2]
    }
    return render(request, 'home/all-products.html', context)


def filterView(request):
    value = int(request.GET.get('sort'))
    path = request.GET.get('path')
    colors = request.GET.getlist('filter[color][]')
    sizes = request.GET.getlist('filter[size][]')
    # products = Product.objects.filter()
    if value == 1:
        products = Product.objects.all().order_by('added_date')
    elif value == 2:
        products = Product.objects.all().order_by('-added_date')
    elif value == 3:
        products = Product.objects.all().order_by('product_new_price')
    elif value == 4:
        products = Product.objects.all().order_by('-product_new_price')
    elif value == 5:
        products = Product.objects.all().order_by('product_name')
    elif value == 6:
        products = Product.objects.all().order_by('-product_name')
    if len(colors) > 0:
        for color in colors:
            products = products.filter(product_colors__color=color)

    if len(sizes) > 0:
        for size in sizes:
            products = products.filter(product_sizes__size=size)
    # print(products)
    # print(path)
    context = {
        'products': products,
        'path': path,
    }

    return render(request, 'home/products-filter.html', context)

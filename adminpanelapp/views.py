from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from adminpanelapp.forms import AdminLoginForm, EditUserForm, AddCategoryForm, AddSubCategoryForm, AddCompanyForm, \
    EditCompanyForm, AddProductForm, EditProductForm, EditProductImagesForm, AddCouponForm
from django.utils.translation import gettext_lazy as _
from userapp.models import User
from ecomapp.models import Category, SubCategory, Company
from productapp.models import Product, ProductImages, Colors, Sizes, Coupon
from django.forms import inlineformset_factory
import html, bleach
import settings


# Create your views here.
def permission_check(user):
    return user.is_staff and user.is_superuser and user.is_active


def adminloginview(request):
    form = AdminLoginForm()
    error_messages = None

    if request.method == 'POST':
        form = AdminLoginForm(data=request.POST)
        email = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user:
            if user.is_active:
                if user.is_staff and user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect(reverse('admin_app:adminindex'))
                else:
                    error_messages = "You Don't have permission to Login this page"
    context = {
        'error_messages': error_messages,
        'form': form,
    }
    return render(request, 'adminpanel/adminlogin.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def adminlogoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('admin_app:admin-login'))


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def adminindexview(request):
    users = User.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'adminpanel/home.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def alluserview(request):
    users = User.objects.all().exclude(username='admin')
    context = {
        'users': users,
    }

    return render(request, 'adminpanel/user-all.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def singleuserview(request, user_pk):
    selected_user = User.objects.get(pk=user_pk)
    context = {
        'selected_user': selected_user,
    }
    return render(request, 'adminpanel/user-single.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def singleusereditview(request, user_pk):
    selected_user = User.objects.get(pk=user_pk)
    form = EditUserForm(instance=selected_user.user_profile)
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=selected_user.user_profile)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = selected_user
            user_obj.save()
            nexts = request.POST.get('next', '/')
            return HttpResponseRedirect(nexts)

    context = {
        'selected_user': selected_user,
        'form': form,
    }
    return render(request, 'adminpanel/user-single-edit.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def orderdetailsview(request):
    context = {

    }
    return render(request, 'adminpanel/order-details.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def allorderview(request):
    context = {

    }
    return render(request, 'adminpanel/order.html', context)


# Category Section Start
@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def addcategoryview(request):
    form = AddCategoryForm()
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context = {
        'form': form,
    }

    return render(request, 'adminpanel/addcategory.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def editcategoryview(request, cat_pk):
    category_item = Category.objects.get(pk=cat_pk)
    if request.method == 'POST':
        category = request.POST.get('cat-edit')
        category_item.category_name = category
        category_item.save()

    return redirect(request.META['HTTP_REFERER'])


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def deletecategoryview(request, cat_pk):
    category_item = Category.objects.get(pk=cat_pk)
    category_item.delete()
    return redirect(request.META['HTTP_REFERER'])


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def validate_category(request):
    category_input = request.POST.get('category_name', None)
    response = {
        'exists': Category.objects.filter(category_name__iexact=category_input).exists()
    }
    return JsonResponse(response)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def viewcategoryview(request):
    category = Category.objects.all()
    return JsonResponse(
        {
            'data': list(category.values())
        }
    )


# Category Section End
# Sub Category Section Start
@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def addsubcategoryview(request):
    form = AddSubCategoryForm()
    if request.method == 'POST':
        form = AddSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
    }

    return render(request, 'adminpanel/addsubcategory.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def viewsubcategoryview(request):
    sub_category = SubCategory.objects.all()
    return JsonResponse(
        {
            'data': list(sub_category.values())
        }
    )


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def deletesubcategoryview(request, sub_cat_pk):
    sub_category = SubCategory.objects.get(pk=sub_cat_pk)
    sub_category.delete()
    return redirect(request.META['HTTP_REFERER'])


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def editsubcategoryview(request, sub_cat_pk):
    sub_category = SubCategory.objects.get(pk=sub_cat_pk)
    form = AddSubCategoryForm(instance=sub_category)
    if request.method == 'POST':
        form = AddSubCategoryForm(request.POST, instance=sub_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_app:add-sub-categories'))
    context = {
        'form': form,
    }
    return render(request, 'adminpanel/editsubcategory.html', context)


# Sub Category Section End

# Manufacturer Section Starts
@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def addmanufacturerview(request):
    form = AddCompanyForm()
    if request.method == 'POST':
        form = AddCompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
    context = {
        'form': form,
    }

    return render(request, 'adminpanel/addmanufacturer.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def viewmanufaturerview(request):
    companies = Company.objects.all()
    return JsonResponse(
        {
            'data': list(companies.values())
        }
    )


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def deletemanufacturerview(request, man_pk):
    company = Company.objects.get(pk=man_pk)
    company.delete()
    return redirect(request.META['HTTP_REFERER'])


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def editmanufacturerview(request, man_pk):
    company = Company.objects.get(pk=man_pk)
    form = EditCompanyForm(instance=company)
    if request.method == 'POST':
        form = EditCompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admin_app:add-manufacturer"))
    context = {
        'form': form
    }
    return render(request, 'adminpanel/editmanufacturer.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def validate_manufacturer(request):
    company_input = request.POST.get('company_name', None)
    response = {
        'exists': Company.objects.filter(company_name__iexact=company_input).exists()
    }
    return JsonResponse(response)


# Product Section Starts
@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def allproductsview(request):
    products = Product.objects.all()
    product_image = ProductImages.objects.all()
    context = {
        'products': products,
        'product_image': product_image,
    }

    return render(request, 'adminpanel/allproducts.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def load_subcategories(request):
    category = request.GET.get('product_category')
    subcategories = SubCategory.objects.filter(category_name_id=category)
    context = {
        'subcategories': subcategories,
    }
    return render(request, 'adminpanel/subcategory_dropdown.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def addproductsview(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    companies = Company.objects.all()
    colors = Colors.objects.all()
    sizes = Sizes.objects.all()
    form = AddProductForm()
    inlineforms = inlineformset_factory(Product, ProductImages, fields=('product_image',), can_delete=False)
    if request.method == 'POST':
        length = request.POST.get('length')
        product_category = request.POST.get('product_category')
        product_subcategory = request.POST.get('product_subcategory')
        product_name = request.POST.get('product_name')
        product_company = request.POST.get('product_company')
        product_quantity = request.POST.get('product_quantity')
        product_price = request.POST.get('product_price')
        product_discount = request.POST.get('product_discount')
        product_description = request.POST.get('product_description')
        product_colors = request.POST.get('product_colors')
        product_sizes = request.POST.get('product_sizes')

        cat_name = Category.objects.get(pk=product_category)
        subcat_name = SubCategory.objects.get(pk=product_subcategory)
        com_name = Company.objects.get(pk=product_company)
        product_colors = list(product_colors.replace(',', ''))
        product_sizes = list(product_sizes.replace(',', ''))
        # print(product_colors)
        # print(product_sizes)

        product_description = bleach.clean(html.unescape(product_description), tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES, styles=settings.STYLES, strip=True, strip_comments=True)

        product_obj = Product.objects.create(
            category_name=cat_name,
            subcategory_name=subcat_name,
            product_name=product_name,
            company_name=com_name,
            product_quantity=int(product_quantity),
            product_price=int(product_price),
            product_discount=int(product_discount),
            product_description=product_description,

        )

        for color in product_colors:
            pro_colors = Colors.objects.get(pk=color)
            product_obj.product_colors.add(pro_colors)
        for size in product_sizes:
            pro_sizes = Sizes.objects.get(pk=size)
            product_obj.product_sizes.add(pro_sizes)

        for file_num in range(0, int(length)):
            ProductImages.objects.create(
                product=product_obj,
                product_image=request.FILES.get(f'images{file_num}')
            )
            # product_image = request.FILES.get(f'images{file_num}')

            # print(product_image)

        images = request.FILES.get('images')
        # print(request.POST)
        # print(length)
        # print(images)

        # return None
    context = {
        'form': form,
        'inlineform': inlineforms(),
        'categories': categories,
        'subcategories': subcategories,
        'companies': companies,
        'colors': colors,
        'sizes': sizes,
    }

    return render(request, 'adminpanel/addproducts.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def editproductsview(request, product_pk):
    # if request.method == 'POST':
    #     length = request.POST.get('length')
    #     product_category = request.POST.get('product_category')
    #     product_subcategory = request.POST.get('product_subcategory')
    #     product_name = request.POST.get('product_name')
    #     product_company = request.POST.get('product_company')
    #     product_quantity = request.POST.get('product_quantity')
    #     product_price = request.POST.get('product_price')
    #     product_discount = request.POST.get('product_discount')
    #     product_description = request.POST.get('product_description')
    #     product_colors = request.POST.get('product_colors')
    #     product_sizes = request.POST.get('product_sizes')
    #
    #     product = Product.objects.create(
    #         category_name=Category.objects.get(pk=product_category),
    #         subcategory_name=SubCategory.objects.get(pk=product_subcategory),
    #         product_name=product_name,
    #         company_name=Company.objects.get(pk=product_company),
    #         product_quantity=int(product_quantity),
    #         product_price=int(product_price),
    #         product_discount=int(product_discount),
    #         product_description=product_description,
    #
    #     )
    #     product.product_colors.set(product_colors)
    #     product.product_sizes.set(product_sizes)
    #
    #     for file_num in range(0, int(length)):
    #         ProductImages.objects.create(
    #             product=product.pk,
    #             product_image=request.FILES.get(f'images{file_num}')
    #         )
    current_product = Product.objects.get(pk=product_pk)
    current_product_images = ProductImages.objects.filter(product=current_product)
    # current_product_sizes = Sizes.objects.filter()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    companies = Company.objects.all()
    colors = Colors.objects.all()
    sizes = Sizes.objects.all()
    form = EditProductForm(instance=current_product)
    form2 = []
    for current_product_image in current_product_images:
        form2.append(EditProductImagesForm(instance=current_product_image))

    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=current_product)
        # form3 = []
        # for current_product_image in current_product_images:
        #     form3.append(EditProductImagesForm(request.POST, request.FILES, instance=current_product_image))
        if form.is_valid():
            model = form.save(commit=False)
            # print(model.product_description)
            model.product_description = bleach.clean(html.unescape(model.product_description), tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES,
                                      styles=settings.STYLES, strip=True, strip_comments=True)
            model.save()

            return HttpResponseRedirect(reverse('admin_app:all-products'))
            # return redirect(request.META['HTTP_REFERER'])

        # print(form3)
        # for image_form in form3:
        #     if image_form.is_valid():
        #         print(image_form)
        #         image_form.save()
        #         print('Hello')

    context = {
        'form': form,
        'form2': form2,
        'product_pk': product_pk,

        'current_product': current_product,
        'current_product_images': current_product_images,

        'current_category': current_product.category_name,
        'current_subcategory': current_product.subcategory_name,
        'current_name': current_product.product_name,
        'current_company': current_product.company_name,
        'current_quantity': current_product.product_quantity,
        'current_price': current_product.product_price,
        'current_discount': current_product.product_discount,
        'current_new_price': current_product.product_new_price,
        'current_sizes': current_product.product_sizes,
        'current_colors': current_product.product_colors,

        'categories': categories,
        'subcategories': subcategories,
        'companies': companies,
        'colors': colors,
        'sizes': sizes,
    }


    return render(request, 'adminpanel/editproducts.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def editproductsimageview(request, product_pk):
    current_product = Product.objects.get(pk=product_pk)
    current_product_images = ProductImages.objects.filter(product=current_product)
    # form = EditProductImagesForm(instance=current_product_images)
    form = []
    for current_product_image in current_product_images:
        form.append(EditProductImagesForm(instance=current_product_image))
    print(form)
    if request.method == 'POST':
        print(request.FILES)
        c = 0
        print('test')
        for item in form:
            # print(item.instance.product_image)
            item = EditProductImagesForm(request.POST, request.FILES, instance=item.instance)
            print(item)
            # print(item.instance.product_image)

            print(item.is_valid())

            if item.is_valid():
                item.save()
        # for current_product_image in current_product_images:
        #     print(current_product_image.product_image)
            # f = EditProductImagesForm(request.POST, request.FILES, instance=current_product_image)
            # print(f)
            # if f.is_valid():
            #     f.save()
            #     c+=1
            #     print(c)

    context = {
        'form': form,
        'product_pk': product_pk,
    }

    return render(request, 'adminpanel/editproductsimages.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def deleteproductsview(request, product_pk):
    current_product = Product.objects.get(pk=product_pk)
    current_product.delete()
    return redirect(request.META['HTTP_REFERER'])


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def addcouponview(request):
    all_coupons = Coupon.objects.all()
    form = AddCouponForm()

    if request.method == 'POST':
        form = AddCouponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context = {
        'all_coupons': all_coupons,
        'form': form,
    }
    return render(request, 'adminpanel/addcoupons.html', context)

@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def viewcouponview(request):
    all_coupons = Coupon.objects.all()


    return JsonResponse(
        {
            'data': list(all_coupons.values())
        }
    )


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def validate_coupons(request):
    coupon_input = request.POST.get('coupon_code', None)
    response = {
        'exists': Coupon.objects.filter(coupon_code__iexact=coupon_input).exists()
    }
    return JsonResponse(response)



@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def editcouponsview(request, coupon_pk):
    coupon_item = Coupon.objects.get(pk=coupon_pk)
    form = AddCouponForm(instance=coupon_item)
    if request.method == 'POST':
        form = AddCouponForm(request.POST, instance=coupon_item)
        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse('admin_app:add-coupons'))

    context = {
        'form': form,
    }
    return render(request, 'adminpanel/editcoupons.html', context)


@user_passes_test(permission_check, login_url='/adminpanel/adminlogin/')
def deletecouponsview(request, coupon_pk):
    coupon_item = Coupon.objects.get(pk=coupon_pk)
    coupon_item.delete()
    return redirect(request.META['HTTP_REFERER'])


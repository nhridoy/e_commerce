from django import forms
from userapp.models import User
from adminpanelapp.models import Profile
from ecomapp.models import Category, SubCategory, Company
from productapp.models import Product, ProductImages, Coupon
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg mb-4', 'placeholder': 'Email', 'autofocus': True,
               'type': 'email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    class Meta:
        model = User
        fields = '__all__'


class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('user',)


class AddCategoryForm(forms.ModelForm):
    category_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Category Name (e.g. Electronics/Garments etc.)'}))

    class Meta:
        model = Category
        fields = '__all__'


class AddSubCategoryForm(forms.ModelForm):
    # category = forms.ModelChoiceField(widget=forms.Select(attrs={'style': 'width:50%'}), queryset=Category.objects.all())
    # subcategory_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Sub Category Name (e.g. Phone/T-Shirts etc.)', 'style': 'width:50%'}))
    subcategory_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Sub Category Name (e.g. Phone/T-Shirts etc.)'}))

    class Meta:
        model = SubCategory
        fields = '__all__'


class AddCompanyForm(forms.ModelForm):
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Company Name (e.g. Samsung/Nokia etc.)'}))
    company_logo = forms.ImageField(help_text='Size Recommended: 256x256',
                                    widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        fields = '__all__'


class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class AddProductForm(forms.ModelForm):
    product_description = SummernoteTextFormField()

    class Meta:
        model = Product

        fields = ('product_description',)
        # widgets = {
        #     'product_description': SummernoteWidget()
        # }


class EditProductForm(forms.ModelForm):
    product_description = SummernoteTextFormField()
    # # Making Field Readonly and ignored by the Database
    product_new_price = forms.CharField(widget=forms.TextInput(attrs={'readonly': ''}))

    class Meta:
        model = Product

        fields = '__all__'
        exclude = ('product_slug',)

    # # Making Field Readonly
    # def __init__(self, *args, **kwargs):
    #     super(EditProductForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.id:
    #         self.fields['product_new_price'].widget.attrs['readonly'] = True
    #
    # # Making Readonly field ignored to the DataBase
    # def clean_foo_field(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.id:
    #         return instance.foo_field
    #     else:
    #         return self.cleaned_data['product_new_price']


class EditProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages

        fields = ('product_image',)


class AddCouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'

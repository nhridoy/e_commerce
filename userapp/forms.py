from django import forms
from userapp.models import User
from adminpanelapp.models import Profile, BillingAddress, ShippingAddress
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'email@emai.com'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'email@emai.com'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2', 'placeholder': 'password'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(
        attrs={'class': 'px-3 bg-gray-100 py-2 border outline-none w-full my-2',
               'placeholder': 'password confirmation'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)


class EditBillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = '__all__'
        exclude = ('user',)


class EditShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ('user',)

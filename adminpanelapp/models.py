from django.db import models
from userapp.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

def get_profile_images_filepath(self, filename):
    return f"users/{self.pk}/{'profile-pic.png'}"


def default_profile_image():
    return f"face1.jpg"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to=get_profile_images_filepath, default=default_profile_image,
                                    verbose_name="Profile Picture")
    full_name = models.CharField(verbose_name="Full Name", max_length=100)
    phone_one = models.CharField(max_length=20, blank=False)
    phone_two = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name_plural = 'Profiles'


class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_billing_address')
    name = models.CharField(max_length=100, verbose_name="Billing User's Full Name")
    phone = models.CharField(max_length=20, verbose_name="Billing User's Phone Number")
    address = models.CharField(max_length=500, verbose_name="Full Address",
                               help_text="(House No., Flat No., Road Name/No., Village/Area, Thana, Post Office)")
    post_code = models.CharField(max_length=20, verbose_name="Post Code")
    district = models.CharField(max_length=100, verbose_name="District")
    state = models.CharField(max_length=100, verbose_name="State")
    country = models.CharField(max_length=100, verbose_name="Country")

    def get_full_address(self):
        return f'{self.address}, {self.post_code}, {self.district}, {self.state}, {self.country}'

    def __str__(self):
        return f"{self.user.username}'s Billing Address"

    def is_fully_filled(self):
        """ Checks if all the fields have been filled """
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False

        return True

    class Meta:
        verbose_name_plural = 'Billing Addresses'


class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_shipping_address')
    name = models.CharField(max_length=100, verbose_name="Shipping User's Full Name")
    phone = models.CharField(max_length=20, verbose_name="Shipping User's Phone Number")
    address = models.CharField(max_length=500, verbose_name="Full Address",
                               help_text="(House No., Flat No., Road Name/No., Village/Area, Thana, Post Office)")
    post_code = models.CharField(max_length=20, verbose_name="Post Code")
    district = models.CharField(max_length=100, verbose_name="District")
    state = models.CharField(max_length=100, verbose_name="State")
    country = models.CharField(max_length=100, verbose_name="Country")

    def get_full_address(self):
        return f'{self.address}, {self.post_code}, {self.district}, {self.state}, {self.country}'

    def __str__(self):
        return f"{self.user.username}'s Shipping Address"

    def is_fully_filled(self):
        """ Checks if all the fields have been filled """
        fields_names = [f.name for f in self._meta.get_fields()]

        for field_name in fields_names:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False

        return True

    class Meta:
        verbose_name_plural = 'Shipping Addresses'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        BillingAddress.objects.create(user=instance)
        ShippingAddress.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.user_profile.save()
    instance.user_billing_address.save()
    instance.user_shipping_address.save()

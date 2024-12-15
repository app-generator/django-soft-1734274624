# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Product(models.Model):

    #__Product_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    info = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    #__Product_FIELDS__END

    class Meta:
        verbose_name        = _("Product")
        verbose_name_plural = _("Product")


class Sales(models.Model):

    #__Sales_FIELDS__
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    units = models.IntegerField(null=True, blank=True)
    sales_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Sales_FIELDS__END

    class Meta:
        verbose_name        = _("Sales")
        verbose_name_plural = _("Sales")



#__MODELS__END

from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.GoodInCart)
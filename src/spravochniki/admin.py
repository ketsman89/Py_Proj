from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Autor)
admin.site.register(models.Serie)
admin.site.register(models.Genre)
admin.site.register(models.Publisher)
admin.site.register(models.Book)
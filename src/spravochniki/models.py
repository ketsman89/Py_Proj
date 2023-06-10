from django.db import models

# Create your models here.

class Book(models.Model):
    autor = models.ForeignKey(
        "spravochniki.Autor",
        on_delete=models.PROTECT,
        verbose_name="Autor",
    )
    name = models.CharField(
        verbose_name="Book name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Book description",
        null=True,
        blank=True,
        max_length=255,
    )

    def __str__(self):
        return self.name

class Autor(models.Model):
    serie = models.ForeignKey(
        "spravochniki.Serie",
        on_delete=models.PROTECT,
        verbose_name="Serie",
        default=1
    )
    name = models.CharField(
        verbose_name="Autor name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Autor description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    
class Serie(models.Model):
    genre = models.ForeignKey(
        "spravochniki.Genre",
        on_delete=models.PROTECT,
        verbose_name="Genre",
        default=1
    )
    name = models.CharField(
        verbose_name="Series name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Series description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    publisher = models.ForeignKey(
        "spravochniki.Publisher",
        on_delete=models.PROTECT,
        verbose_name="Genre",
        default=1
    )
    name = models.CharField(
        verbose_name="Genre name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Genre Publisher",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(
        verbose_name="Publisher name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Publisher description",
        null=True,
        blank=True,
    )

#     def __str__(self):
#         return self.name
    

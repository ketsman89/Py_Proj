from django.db import models

# Create your models here.

class Autors(models.Model):
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
    
class Series(models.Model):
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
    name = models.CharField(
        verbose_name="Genre name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Genre description",
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

    def __str__(self):
        return self.name
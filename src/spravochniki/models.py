from django.db import models
from django.urls import reverse_lazy
from PIL import Image
from pathlib import Path
# Create your models here.

class Book(models.Model): 

    name = models.CharField(
        verbose_name="Book name",
        max_length=20,
    )

    picture = models.ImageField(
        verbose_name="Book picture",
        upload_to="uploads/%Y/%m/%d/",
    )
    price = models.DecimalField(
        verbose_name="Book price",
        decimal_places=2,
        max_digits=6
    )
    autor = models.ForeignKey(
        "spravochniki.Autor",
        on_delete=models.PROTECT,
        verbose_name="Autor",
    )
    serie = models.ForeignKey(
        "spravochniki.Serie",
        on_delete=models.PROTECT,
        verbose_name="Serie",
        default=1
    )
    genre = models.ForeignKey(
        "spravochniki.Genre",
        on_delete=models.PROTECT,
        verbose_name="Genre",
        default=1
    )
    year = models.IntegerField(
        verbose_name="Year",
        null=True,
        blank=True,
        
        
    )
    pages = models.IntegerField(
        verbose_name="numbers of pages",
        null=True,
        blank=True,
        
    )
    cover = models.CharField(
        verbose_name="book cover",
        null=True,
        blank=True,
        max_length=10,
    )
    format = models.CharField(
        verbose_name="format",
        null=True,
        blank=True,
        max_length=2,
    )

    isbn = models.CharField(
        verbose_name="isbn",
        null=True,
        blank=True,
        max_length=15,
    )
    weight = models.CharField(
        verbose_name="weight",
        null=True,
        blank=True,
        max_length=5,
        
    )
    age = models.CharField(
        verbose_name="age",
        null=True,
        blank=True,
        max_length=3,
    )

    publisher = models.ForeignKey(
        "spravochniki.Publisher",
        on_delete=models.PROTECT,
        verbose_name="publisher",
        default=1
    )
    numbers = models.IntegerField(
        verbose_name="numbers of book",
        null=True,
        blank=True,
    )
    availability = models.CharField(
        verbose_name="availability",
        max_length=3,
        null=True,
        blank=True,
    )
    rating = models.CharField(
        verbose_name="rating",
        max_length=3,
        null=True,
        blank=True,
    )
    created = models.DateField(
        verbose_name="created",
        null=True,
        blank=True,
    )
    updated = models.DateField(
        verbose_name="updated",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-book', kwargs={"pk": self.pk})
    
    def get_search_url(self):
        return reverse_lazy('spravochniki:view-book', kwargs={"pk": self.pk})
        
    def book_picture_med(self):
        original_url = self.picture.url
        new_url = original_url.split(".")
        picture_url = ".".join(new_url[:-1]) + "_150_." + new_url[-1]
        return picture_url
    
    def book_picture_small(self):
        original_url = self.picture.url
        new_url = original_url.split(".")
        picture_url = ".".join(new_url[:-1]) + "_40_." + new_url[-1]
        return picture_url
    
    def picture_resizer(self):
        extention = self.picture.file.name.split('.')[-1]
        BASE_DIR = Path(self.picture.file.name).resolve().parent
        file_name = Path(self.picture.file.name).resolve().name.split('.')
        for m_basewidth in [150, 40]:
            im = Image.open(self.picture.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))    
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(str(BASE_DIR / ".".join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)

class Autor(models.Model):
    
    name = models.CharField(
        verbose_name="Autor name",
        max_length=20,
    )
    description = models.TextField(
        verbose_name="Autor description",
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return f"/autor/(self.pk)"

    def __str__(self):
        return self.name
    
class Serie(models.Model):
    
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
    
class Status(models.Model):
    name = models.CharField(
        verbose_name="Status name",
        max_length=20,
    )
    def __str__(self):
        return self.name
    
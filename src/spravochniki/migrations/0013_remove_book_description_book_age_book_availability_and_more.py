# Generated by Django 4.2.1 on 2023-06-18 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0012_book_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='age'),
        ),
        migrations.AddField(
            model_name='book',
            name='availability',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='availability'),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='book cover'),
        ),
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateField(blank=True, null=True, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='book',
            name='format',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='format'),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='isbn'),
        ),
        migrations.AddField(
            model_name='book',
            name='numbers',
            field=models.IntegerField(blank=True, null=True, verbose_name='numbers of book'),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True, verbose_name='numbers of pages'),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6, verbose_name='Book price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='rating'),
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateField(blank=True, null=True, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='weight'),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Year'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='spravochniki.publisher', verbose_name='publisher'),
        ),
    ]

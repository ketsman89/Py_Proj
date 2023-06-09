# Generated by Django 4.2.1 on 2023-06-13 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0010_genre_publisher_serie_genre_alter_autor_serie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='serie',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='spravochniki.genre', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='spravochniki.publisher', verbose_name='Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='serie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='spravochniki.serie', verbose_name='Serie'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0005_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='Book description'),
        ),
    ]

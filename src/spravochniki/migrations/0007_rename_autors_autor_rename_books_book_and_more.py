# Generated by Django 4.2.1 on 2023-06-10 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0006_alter_books_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Autors',
            new_name='Autor',
        ),
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Series',
            new_name='Serie',
        ),
    ]
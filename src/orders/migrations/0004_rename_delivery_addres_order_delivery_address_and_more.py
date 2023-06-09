# Generated by Django 4.2.1 on 2023-06-27 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0017_status'),
        ('orders', '0003_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivery_addres',
            new_name='delivery_address',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='spravochniki.status', verbose_name='Order status'),
            preserve_default=False,
        ),
    ]

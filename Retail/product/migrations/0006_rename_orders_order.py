# Generated by Django 3.2.9 on 2022-01-09 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]

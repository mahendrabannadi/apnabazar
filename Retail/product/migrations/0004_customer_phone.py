# Generated by Django 3.2.9 on 2022-01-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default=1, max_length=22),
            preserve_default=False,
        ),
    ]

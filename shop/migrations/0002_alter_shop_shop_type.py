# Generated by Django 3.2.4 on 2021-11-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_type',
            field=models.IntegerField(choices=[(0, 'studio'), (1, 'beautyshop'), (2, 'waxingshop'), (3, 'tanningshop')]),
        ),
    ]

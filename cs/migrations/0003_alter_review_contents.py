# Generated by Django 3.2.4 on 2021-11-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cs', '0002_auto_20211102_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='contents',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-27 06:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_alter_user_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='exp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

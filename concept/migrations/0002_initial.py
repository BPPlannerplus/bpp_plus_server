# Generated by Django 3.2.4 on 2021-07-27 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('concept', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioconcept',
            name='like_users',
            field=models.ManyToManyField(related_name='like_concepts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studioconcept',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio_concepts', to='shop.shop'),
        ),
        migrations.AddField(
            model_name='beautyshopconcept',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beautyshop_concepts', to='shop.shop'),
        ),
    ]

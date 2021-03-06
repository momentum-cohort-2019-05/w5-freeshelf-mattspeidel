# Generated by Django 2.2.2 on 2019-06-29 17:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookindex', '0007_auto_20190628_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_by',
            field=models.ManyToManyField(related_name='favorite_books', through='bookindex.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]

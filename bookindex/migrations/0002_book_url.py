# Generated by Django 2.2.2 on 2019-06-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookindex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(default='https://www.google.com/'),
        ),
    ]
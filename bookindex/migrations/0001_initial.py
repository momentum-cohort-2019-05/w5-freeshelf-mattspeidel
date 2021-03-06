# Generated by Django 2.2.2 on 2019-06-24 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a book genre (e.g. Science Fiction)', max_length=200)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Enter the summary', max_length=1000)),
                ('date_added', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('category', models.ManyToManyField(help_text='Select a genre for this book', to='bookindex.Category')),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-24 21:08

from django.db import migrations
from django.conf import settings
import os
import csv

def load_initial_questions(apps, schema_editor):
    Category = apps.get_model('bookindex', 'Category')
    Book = apps.get_model('bookindex', 'Book')

    Category.objects.all().delete()
    Book.objects.all().delete()

    category = Category(name="Programming books")
    category.save()

    filename = os.path.join(settings.BASE_DIR, 'sample_books.csv')

    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            book = Book(title=row['title'], author=row['author'], description=row['description'], url=row['url'])
            book.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bookindex', '0002_book_url'),
    ]

    operations = [migrations.RunPython(load_initial_questions)]
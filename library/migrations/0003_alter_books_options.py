# Generated by Django 5.1.4 on 2025-01-24 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_movies_books'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'книга', 'verbose_name_plural': 'книги'},
        ),
    ]

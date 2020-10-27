# Generated by Django 2.2 on 2020-10-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0011_authors_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='books',
        ),
        migrations.AddField(
            model_name='authors',
            name='book',
            field=models.ManyToManyField(related_name='author', to='books_authors_app.Books'),
        ),
    ]
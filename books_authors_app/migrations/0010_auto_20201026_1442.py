# Generated by Django 2.2 on 2020-10-26 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0009_auto_20201026_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='notes',
        ),
        migrations.AlterField(
            model_name='books',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
# Generated by Django 2.2 on 2020-10-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0007_auto_20201026_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='notes',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='books',
            name='desc',
            field=models.TextField(blank=True, default=None),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2023-01-14 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20230114_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='created_by',
            new_name='author',
        ),
    ]

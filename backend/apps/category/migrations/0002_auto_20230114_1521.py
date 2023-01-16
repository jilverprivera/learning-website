# Generated by Django 3.2.7 on 2023-01-14 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('date_created',), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ('date_created',), 'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='created_at',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='created_at',
            new_name='date_created',
        ),
    ]
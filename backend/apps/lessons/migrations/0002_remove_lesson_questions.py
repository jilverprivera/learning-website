# Generated by Django 3.2.7 on 2023-01-15 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='questions',
        ),
    ]
# Generated by Django 3.2.7 on 2023-01-15 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='lessons',
        ),
    ]

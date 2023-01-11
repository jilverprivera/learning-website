# Generated by Django 3.2.7 on 2023-01-11 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_auto_20230111_1119'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votes',
            new_name='Vote',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('trialing', 'Trialing')], default='pending', max_length=32),
        ),
        migrations.CreateModel(
            name='PaidCoursesLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('courses', models.ManyToManyField(blank=True, to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Purchased Courses Library',
            },
        ),
        migrations.CreateModel(
            name='CoursesLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('courses', models.ManyToManyField(blank=True, to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Bookmarked Courses Library',
            },
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grades',
            name='assignment',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='course',
        ),
        migrations.RemoveField(
            model_name='grades',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='course',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='video',
        ),
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, upload_to='assets/images/lesson/'),
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Grades',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]

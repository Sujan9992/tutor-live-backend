# Generated by Django 4.0.3 on 2022-06-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/images/lesson/'),
        ),
    ]
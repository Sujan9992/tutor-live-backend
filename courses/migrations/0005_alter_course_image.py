# Generated by Django 4.0.3 on 2022-06-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_assignment_q1option3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/images/course/'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-06-05 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_grades_assignment_remove_grades_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('question1', models.TextField(blank=True)),
                ('q1option1', models.CharField(blank=True, max_length=200)),
                ('q1option2', models.CharField(blank=True, max_length=200)),
                ('q1option3', models.CharField(blank=True, max_length=200)),
                ('q1option4', models.CharField(blank=True, max_length=200)),
                ('question2', models.TextField(blank=True)),
                ('q2option1', models.CharField(blank=True, max_length=200)),
                ('q2option2', models.CharField(blank=True, max_length=200)),
                ('q2option3', models.CharField(blank=True, max_length=200)),
                ('q2option4', models.CharField(blank=True, max_length=200)),
                ('question3', models.TextField(blank=True)),
                ('q3option1', models.CharField(blank=True, max_length=200)),
                ('q3option2', models.CharField(blank=True, max_length=200)),
                ('q3option3', models.CharField(blank=True, max_length=200)),
                ('q3option4', models.CharField(blank=True, max_length=200)),
                ('question4', models.TextField(blank=True)),
                ('q4option1', models.CharField(blank=True, max_length=200)),
                ('q4option2', models.CharField(blank=True, max_length=200)),
                ('q4option3', models.CharField(blank=True, max_length=200)),
                ('q4option4', models.CharField(blank=True, max_length=200)),
                ('question5', models.TextField(blank=True)),
                ('q5option1', models.CharField(blank=True, max_length=200)),
                ('q5option2', models.CharField(blank=True, max_length=200)),
                ('q5option3', models.CharField(blank=True, max_length=200)),
                ('q5option4', models.CharField(blank=True, max_length=200)),
                ('answer1', models.TextField(blank=True)),
                ('answer2', models.TextField(blank=True)),
                ('answer3', models.TextField(blank=True)),
                ('answer4', models.TextField(blank=True)),
                ('answer5', models.TextField(blank=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]

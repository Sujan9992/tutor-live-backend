from email.mime import image
from django.db import models
from account.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='assets/images/course/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CourseSchedule(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    sunday = models.CharField(max_length=100, blank=True)
    monday = models.CharField(max_length=100, blank=True)
    tuesday = models.CharField(max_length=100, blank=True)
    wednesday = models.CharField(max_length=100, blank=True)
    thursday = models.CharField(max_length=100, blank=True)
    friday = models.CharField(max_length=100, blank=True)
    saturday = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class EnrolledCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title

class Lesson(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='assets/images/lesson/', blank=True, null=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    question1 = models.TextField(blank=True)
    q1option1 = models.CharField(max_length=200, blank=True)
    q1option2 = models.CharField(max_length=200, blank=True)
    question2 = models.TextField(blank=True)
    q2option1 = models.CharField(max_length=200, blank=True)
    q2option2 = models.CharField(max_length=200, blank=True)
    question3 = models.TextField(blank=True)
    q3option1 = models.CharField(max_length=200, blank=True)
    q3option2 = models.CharField(max_length=200, blank=True)
    question4 = models.TextField(blank=True)
    q4option1 = models.CharField(max_length=200, blank=True)
    q4option2 = models.CharField(max_length=200, blank=True)
    question5 = models.TextField(blank=True)
    q5option1 = models.CharField(max_length=200, blank=True)
    q5option2 = models.CharField(max_length=200, blank=True)
    answer1 = models.TextField(blank=True)
    answer2 = models.TextField(blank=True)
    answer3 = models.TextField(blank=True)
    answer4 = models.TextField(blank=True)
    answer5 = models.TextField(blank=True)

    def __str__(self):
        return self.title

class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.course.title

# class Grades(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     grade = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.course.title

# class Rating(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     rating = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.course.title
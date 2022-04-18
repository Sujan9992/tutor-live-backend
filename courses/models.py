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
    image = models.ImageField(upload_to='images/course/', blank=True)
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

# Delete these models if you don't want to use them
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.full_name

# Delete these models if you don't want to use them
class UserCourses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.user.full_name

class EnrolledCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.title
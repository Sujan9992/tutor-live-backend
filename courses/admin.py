from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'title', 'category']
    list_filter = ['created_by']
    search_fields = ['title', 'keywords',]

class CourseScheduleAdmin(admin.ModelAdmin):
    list_display = ['course_id',]
    list_filter = ['course_id',]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']

class EnrolledCoursesAdmin(admin.ModelAdmin):
    list_display = ['user']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'title']
    list_filter = ['course_id',]

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'title']
    list_filter = ['course_id',]

class CourseProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'course_id']
    list_filter = ['user', 'course_id']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseSchedule, CourseScheduleAdmin)
admin.site.register(EnrolledCourses, EnrolledCoursesAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(CourseProgress, CourseProgressAdmin)
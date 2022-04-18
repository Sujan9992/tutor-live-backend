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

class UserCoursesAdmin(admin.ModelAdmin):
    list_display = ['user',]

class TutorAdmin(admin.ModelAdmin):
    list_display = ['user']

class EnrolledCoursesAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserCourses, UserCoursesAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(CourseSchedule, CourseScheduleAdmin)
admin.site.register(EnrolledCourses, EnrolledCoursesAdmin)
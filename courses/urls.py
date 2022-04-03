from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('courses/', courseView, name='courses'),
    path('manage_course/<int:course_id>/', manageCourseView, name='manage_course'),
    path('categories/', categoryView, name='categories'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('course_schedule/<int:course_id>/', courseScheduleView, name='course_schedule'),
    path('all_schedules/', getAllCoursesSchedule, name='all_schedules'),
    path('get_courses_by_category/<str:title>/', getCoursesByCategory, name='get_courses_by_category'),
    path('get_courses_by_user/', getCoursesByCurrentUser, name='get_courses_by_user'),
    path('get_courses_by_user/<int:user_id>/', getCoursesByUser, name='get_courses_by_user'),
]
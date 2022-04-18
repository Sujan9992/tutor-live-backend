from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('courses/', courseView, name='courses'),
    path('manage_course/<int:course_id>/', manageCourseView, name='manage_course'),
    path('categories/', categoryView, name='categories'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('course_schedule/<int:course_id>/', courseScheduleView, name='course_schedule'),
    path('all_schedules/', getAllCoursesSchedule, name='all_schedules'),
    path('courses_by_category/<str:title>/', getCoursesByCategory, name='courses_by_category'),
    path('courses_created_by_current_user/', getCoursesCreatedByCurrentUser, name='courses_by_current_user'),
    path('courses_created_by_user/<int:user_id>/', getCoursesCreatedByUser, name='courses_by_user'),
    path('enrolled_courses/<int:user_id>/', getEnrolledCoursesByUser, name='enrolled_courses'),
    path('get_tutors/', getTutors, name='get_tutors'),
    path('getTutorsByCategory/<str:title>/', getTutorsByCategory, name='get_tutors_by_category'),
]
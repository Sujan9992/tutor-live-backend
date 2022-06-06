from rest_framework import serializers
from common.serializers import Base64ImageField
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class CourseSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None,use_url = True, required=False)
    class Meta:
        model = Course
        fields = ['course_id', 'title', 'keywords', 'description', 'image',
                  'category', 'created_by',
                  ]

class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = ['course_id', 'title', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

class LessonSerializer(serializers.ModelSerializer):
    image = Base64ImageField(max_length=None,use_url = True, required=False)
    class Meta:
        model = Lesson
        fields = ['course_id', 'title', 'description', 'image']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['course_id', 'title', 'question1', 'q1option1', 'q1option2', 'answer1', 'answer2', 'answer3', 'answer4', 'question2', 'question3', 'question4', 'question5',
                  'q2option1', 'q2option2', 'q3option1', 'q3option2', 'q4option1', 'q4option2', 'q5option1', 'q5option2']

class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = ['user', 'course', 'progress']
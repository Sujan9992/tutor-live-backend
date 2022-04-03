from rest_framework import serializers
from .models import *

# class ImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ['image']

# class CourseSPecificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CourseSpecification
#         fields = ['title']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class CourseSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Course
        fields = ['course_id', 'title', 'keywords', 'description', 'image',
                  'category', 'created_by',
                  ]

class CourseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSchedule
        fields = ['course_id', 'title', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def courseView(request):
    if request.method == 'GET':
        user = request.user
        if user:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def manageCourseView(request, course_id):
    try:
        course = Course.objects.get(course_id=course_id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def categoryView(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated])
def courseScheduleView(request, course_id):
    if request.method == 'GET':
        course_schedule = CourseSchedule.objects.get(course_id=course_id)
        serializer = CourseScheduleSerializer(course_schedule)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        course_schedule = CourseSchedule.objects.get(course_id=course_id)
        serializer = CourseScheduleSerializer(course_schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllCoursesSchedule(request):
    if request.method == 'GET':
        course_schedules = CourseSchedule.objects.all()
        serializer = CourseScheduleSerializer(course_schedules, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCoursesByCategory(request, title):
    if request.method == 'GET':
        courses = Course.objects.filter(category=title)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCoursesByCurrentUser(request):
    if request.method == 'GET':
        user = request.user
        courses = Course.objects.filter(created_by=user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCoursesByUser(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        courses = Course.objects.filter(created_by=user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
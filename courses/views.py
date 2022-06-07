from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from account.serializers import UserProfileSerializer

# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
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

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createCourse(request):
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def enrollCourse(request, course_id):
    if request.method == 'POST':
        user = request.user
        if user:
            course = Course.objects.get(course_id=course_id)
            EnrolledCourses.objects.create(user=user, course=course)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
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
# @permission_classes([IsAuthenticated])
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
# @permission_classes([IsAuthenticated])
def courseScheduleView(request, course_id):
    if request.method == 'GET':
        course_schedule = CourseSchedule.objects.get(course_id=course_id)
        serializer = CourseScheduleSerializer(course_schedule)
        return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createSchedule(request, course_id):
    if request.method == 'POST':
        serializer = CourseScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getAllCoursesSchedule(request):
    if request.method == 'GET':
        course_schedules = CourseSchedule.objects.all()
        serializer = CourseScheduleSerializer(course_schedules, many=True)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def enrolledCoursesScheduleView(request):
    if request.method == 'GET':
        user = request.user
        if user:
            user_id = user.id
            enrolledCourses = EnrolledCourses.objects.filter(user_id=user_id)
            courses = []
            for enrolledCourse in enrolledCourses:
                course_id = enrolledCourse.course_id
                course_schedule = CourseSchedule.objects.get(course_id=course_id)
                courses.append(course_schedule)
            serializer = CourseScheduleSerializer(courses, many=True)
            return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCoursesByCategory(request, title):
    if request.method == 'GET':
        courses = Course.objects.filter(category=title)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCoursesCreatedByCurrentUser(request):
    if request.method == 'GET':
        user = request.user
        courses = Course.objects.filter(created_by=user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCoursesCreatedByUser(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        courses = Course.objects.filter(created_by=user)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getEnrolledCourses(request):
    if request.method == 'GET':
        user = request.user
        if user:
            user_id = user.id
            enrolledCourses = EnrolledCourses.objects.filter(user=user_id)
            courses = []
            for enrolledCourse in enrolledCourses:
                course_id = enrolledCourse.course_id
                course = Course.objects.get(course_id=course_id)
                courses.append(course)
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCourseProgress(request, course_id):
    if request.method == 'GET':
        user = request.user
        if user:
            user_id = user.id
            enrolledCourses = EnrolledCourses.objects.filter(user=user_id)
            courses = []
            for enrolledCourse in enrolledCourses:
                course_id = enrolledCourse.course_id
                course = Course.objects.get(course_id=course_id)
                courses.append(course)
            progress = []
            for course in courses:
                course_id = course.course_id
                progress.append(CourseProgress.objects.get(course=course_id))
            serializer = CourseProgressSerializer(progress)
            return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getTutors(request):
    if request.method == 'GET':
        tutors = Course.objects.all().distinct().values('created_by')
        tutorList = []
        for tutor in tutors:
            tutorList.append(User.objects.get(id=tutor['created_by']))
        serializer = UserProfileSerializer(tutorList, many=True)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getTutorsByCategory(request, title):
    if request.method == 'GET':
        tutors = Course.objects.filter(category=title).distinct().values('created_by')
        tutorList = []
        for tutor in tutors:
            tutorList.append(User.objects.get(id=tutor['created_by']))
        serializer = UserProfileSerializer(tutorList, many=True)
        return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getLessonsByCourse(request, course_id):
    if request.method == 'GET':
        lessons = Lesson.objects.filter(course_id=course_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createLesson(request, course_id):
    if request.method == 'POST':
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getCourseAssignment(request, course_id):
    if request.method == 'GET':
        course_assignment = Assignment.objects.get(course_id=course_id)
        serializer = AssignmentSerializer(course_assignment)
        return Response([serializer.data])

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def createAssignment(request, course_id):
    if request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
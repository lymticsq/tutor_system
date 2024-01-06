from django.shortcuts import render

from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from myapp.models import CustomUser, Teacher, Student
from myapp.serializers import CustomUserSerializer

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['post'])
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')
        name = request.data.get('name')
        # 判断用户名是否已存在(存在直接返回400)
        if CustomUser.objects.filter(username=username).exists():
            return Response({'description':'User already exists!'},status=status.HTTP_400_BAD_REQUEST)
        # 根据请求体的role来创建学生或者教师信息
        role_id = 0
        if role == 'teacher':
            teacher = Teacher.objects.create(name=name)
            role_id = teacher.id
        elif role == 'student':
            student = Student.objects.create(name=name)
            role_id = student.id

        user = CustomUser.objects.create_user(username=username, password=password, role=role, role_id=role_id)
        user.save()
        return Response({'message': 'User registered successfully'}, status=status.HTTP_200_OK)
    # 登录
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            token,created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong user name or password!'}, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

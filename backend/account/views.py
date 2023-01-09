from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['image'] = user.image.url
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        token['is_active'] = user.is_active
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        user = User.objects.all()
        print(user)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getUserByID(request, pk):
    if request.method == 'GET':
        user = User.objects.all().filter(id=pk)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getUserByEmail(request, email):
    if request.method == 'GET':
        user = User.objects.all().filter(email=email)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

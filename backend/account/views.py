
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer
from .models import User


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


class UserListView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        users = User.objects.all()
        if len(users) == 0:
            Response({'Success': 'No users found.'}, status=status.HTTP_204_NO_CONTENT)
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)


class SingleUserView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, user_uuid, format=None):
        if not User.objects.filter(uuid=user_uuid).exists():
            Response({'Error': 'User with uuid: {} not found.'.format(user_uuid)}, status=status.HTTP_404_NOT_FOUND)
        user  = User.objects.get(uuid=user_uuid)
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)

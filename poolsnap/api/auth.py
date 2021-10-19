from django.contrib.auth import authenticate, login
from rest_framework import viewsets, serializers, mixins, permissions, status, generics
from rest_framework.exceptions import APIException
from rest_framework_simplejwt.tokens import AccessToken
from poolsnap.models import User


class InvalidCredentialsException(APIException):
    status_code = 404
    default_detail = 'email or password is invalid'
    default_code = 'invalid credentials'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    avatar = serializers.URLField(read_only=True)
    is_admin = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        request = self.context['request']
        user = authenticate(
            request, email=validated_data['email'], password=validated_data['password'])
        if user is None:
            raise InvalidCredentialsException
        return user

    def get_token(self, obj):
        return str(AccessToken.for_user(obj))

    def get_is_admin(self, obj):
        return obj.is_admin


class LoginView(generics.CreateAPIView):
    queryset = User.active_objects.all()
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

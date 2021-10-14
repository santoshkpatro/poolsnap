from django.contrib.auth import authenticate, login
from rest_framework import viewsets, serializers, mixins, permissions, status, generics
from rest_framework_simplejwt.tokens import AccessToken
from poolsnap.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    avatar = serializers.URLField(read_only=True)

    def create(self, validated_data):
        request = self.context['request']
        user = authenticate(request, email=validated_data['email'], password=validated_data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid email or password', code='invalid_credentials')
        return user

    def get_token(self, obj):
        return str(AccessToken.for_user(obj))


class LoginView(generics.CreateAPIView):
    queryset = User.active_objects.all()
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_200_OK
        return response

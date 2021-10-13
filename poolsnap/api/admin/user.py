from rest_framework import viewsets, generics, status, serializers
from poolsnap.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar', 'date_joined', 'last_update', 'is_active']
        extra_kwargs = {
            'email': {
                'read_only': True
            },
            'date_joined': {
                'read_only': True
            },
        }


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

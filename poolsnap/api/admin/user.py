from rest_framework import viewsets, generics, status, serializers, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from poolsnap.models import User, License, Item


class UserSerializer(serializers.ModelSerializer):
    license_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'password', 'last_name',
                  'avatar', 'date_joined', 'last_update', 'is_active', 'license_count']
        extra_kwargs = {
            'date_joined': {
                'read_only': True
            },
            'password': {
                'write_only': True
            }
        }

    def get_license_count(self, obj):
        return obj.user_licenses.all().count()

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'price', 'is_available']


class LicenseSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = License
        fields = ['license_id', 'item', 'is_valid', 'created_at']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    @action(methods=['GET'], detail=True)
    def licenses(self, request, pk):
        user = self.get_object()
        licenses = user.user_licenses.all()
        serializer = LicenseSerializer(licenses, many=True)
        return Response(serializer.data)

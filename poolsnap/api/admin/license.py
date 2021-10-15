from django.db.models import fields
from rest_framework import viewsets, serializers, permissions
from rest_framework.exceptions import APIException
from poolsnap.models import License, User, Item
from poolsnap.exceptions import NotFoundException


class UniqueUserItemException(APIException):
    status_code = 400
    default_detail = 'user and item should be unique'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'resource_url', 'is_available']


class LicenseSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    item_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    class Meta:
        model = License
        fields = ['id', 'license_id', 'user', 'item',
                  'is_valid', 'created_at', 'user_id', 'item_id']
        extra_kwargs = {
            'user': {
                'read_only': True
            },
            'item': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        item_id = validated_data.pop('item_id')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFoundException(detail='user not found')

        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise NotFoundException(detail='item not found')

        try:
            license = License(**validated_data, user=user, item=item)
            license.save()
            return license
        except:
            raise UniqueUserItemException

    def update(self, instance, validated_data):
        user = None
        item = None

        if 'user_id' in validated_data:
            user_id = validated_data.pop('user_id')
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise NotFoundException(detail='user not found')

        if 'item_id' in validated_data:
            item_id = validated_data.pop('item_id')
            try:
                item = Item.objects.get(id=item_id)
            except Item.DoesNotExist:
                raise NotFoundException(detail='item not found')
        license = super().update(instance, validated_data)
        if user:
            license.user = user
        if item:
            license.item = item

        license.save()
        return license


class LicenseViewSet(viewsets.ModelViewSet):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

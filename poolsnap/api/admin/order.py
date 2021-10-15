from rest_framework import viewsets, permissions, serializers
from rest_framework.exceptions import APIException
from poolsnap.models import Order, User, Item
from poolsnap.exceptions import NotFoundException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'avatar']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'price', 'resource_url', 'is_available']


class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    item_id = serializers.IntegerField(write_only=True)
    user = UserSerializer(read_only=True)
    item = ItemSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'order_id', 'user', 'item', 'price', 'discount', 'amount',
                  'status', 'transaction_id', 'payment_id', 'created_at', 'user_id', 'item_id']
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
            order = Order(**validated_data, user=user, item=item)
            order.save()
            return order
        except:
            raise APIException

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
        order = super().update(instance, validated_data)
        if user:
            order.user = user
        if item:
            order.item = item

        order.save()
        return order


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

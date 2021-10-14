from rest_framework import viewsets, serializers, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from poolsnap.models import Item, Category, category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'category', 'title', 'slug', 'description', 'price',
                  'discount', 'is_available', 'created_at', 'category_id', 'resource_url']

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        item = Item(**validated_data)
        if 'category_id' is not None:
            try:
                category = Category.objects.get(id=category_id)
                item.category = category
            except Category.DoesNotExist:
                raise serializers.ValidationError('category error', 'category error')
        item.save()
        return item

    def update(self, instance, validated_data):
        item = super().update(instance, validated_data)
        if 'category_id' in validated_data:
            category_id = validated_data.pop('category_id')
            try:
                category = Category.objects.get(id=category_id)
                item.category = category
                item.save()
            except Category.DoesNotExist:
                raise serializers.ValidationError('category error', 'category error')
        return item


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

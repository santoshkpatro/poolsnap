from rest_framework import viewsets, serializers
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from poolsnap.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'slug', 'description', 'price', 'discount']


class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

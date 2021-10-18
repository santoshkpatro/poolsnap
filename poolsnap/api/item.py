from rest_framework import serializers, viewsets, permissions, generics
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from poolsnap.models import Item, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Item
        fields = ['title', 'category', 'description', 'price', 'discount', 'resource_url']


class ItemViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    serializer_class = ItemSerializer
    queryset = Item.available_objects.all()
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        q = super().get_queryset()
        if 'category' in self.request.query_params:
            category_name = self.request.query_params['category']
            q = q.filter(category__name=category_name)
        return q

    # @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    # def owned(self, request):
    #     q = self.get_queryset()
    #     print(self.request.user.user_licenses.values())
    #     return Response()

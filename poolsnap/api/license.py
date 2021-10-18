from rest_framework import serializers, generics, permissions, viewsets
from poolsnap.models import License, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'price', 'resource_url']


class LicenseSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)

    class Meta:
        model = License
        fields = ['license_id', 'item', 'created_at']


class LicenseViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    serializer_class = LicenseSerializer
    queryset = License.valid_objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(user=self.request.user)

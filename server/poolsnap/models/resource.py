from django.db import models
from .item import Item


class AvailableResourceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Resource(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_resources')
    url = models.URLField()
    size = models.CharField(max_length=10, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available_objects = AvailableResourceManager()

    class Meta:
        db_table = 'resources'

    def __str__(self) -> str:
        return str(self.id)

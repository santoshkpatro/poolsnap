from django.db import models
from .item import Item


class Resource(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_resources')
    size = models.CharField(max_length=10)

    class Meta:
        db_table = 'resources'

    def __str__(self) -> str:
        return str(self.id)

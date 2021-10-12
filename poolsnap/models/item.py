from django.db import models
from .category import Category


class ItemAvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_items')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    available_objects = ItemAvailableManager()

    class Meta:
        db_table = 'items'

    def __str__(self) -> str:
        return self.title

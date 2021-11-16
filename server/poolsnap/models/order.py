import shortuuid
from django.db import models
from .user import User
from .item import Item


class Order(models.Model):
    ORDER_STATUS = (
        ('INITIATED', 'INITIATED'),
        ('PROCESSING', 'PROCESSING'),
        ('COMPLETE', 'COMPLETE'),
        ('DISCARDED', 'DISCARDED')
    )

    order_id = models.CharField(max_length=12, blank=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=10, default='INITIATED', choices=ORDER_STATUS)
    transaction_id = models.CharField(max_length=50, blank=True, null=True)
    payment_id = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders'

    def __str__(self) -> str:
        return self.order_id

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = shortuuid.ShortUUID().random(length=10).upper()
        return super().save(*args, **kwargs)

import shortuuid
from django.db import models
from .user import User
from .item import Item


class ValidLicenseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_valid=True)


class License(models.Model):
    license_id = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_licenses')
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True, related_name='item_licenses')
    is_valid = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    valid_licenses = ValidLicenseManager()

    class Meta:
        db_table = 'licenses'

    def __str__(self) -> str:
        return self.license_id

    def save(self, *args, **kwargs) -> None:
        if not self.license_id:
            self.license_id = shortuuid.ShortUUID().random(length=10).upper()
        return super().save(*args, **kwargs)

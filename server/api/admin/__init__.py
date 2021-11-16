from rest_framework.routers import DefaultRouter
from .user import UserViewSet
from .item import ItemViewSet
from .license import LicenseViewSet
from .order import OrderViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)
router.register(r'licenses', LicenseViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls

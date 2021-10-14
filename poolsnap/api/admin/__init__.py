from rest_framework.routers import DefaultRouter
from .user import UserViewSet
from .item import ItemViewSet

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = router.urls

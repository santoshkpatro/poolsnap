from django.urls import path
from rest_framework.routers import DefaultRouter
from . import auth
from . import item
from . import license
from . import check

router = DefaultRouter()

router.register('items', item.ItemViewSet)
router.register('licenses', license.LicenseViewSet)

urlpatterns = [
    path('health/', check.health),
    path('auth/login/', auth.LoginView.as_view())
]


urlpatterns += router.urls

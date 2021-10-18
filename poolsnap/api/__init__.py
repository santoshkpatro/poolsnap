from django.urls import path
from rest_framework.routers import DefaultRouter
from . import auth
from . import item
from . import license

router = DefaultRouter()

router.register('items', item.ItemViewSet)
router.register('licenses', license.LicenseViewSet)

urlpatterns = [
    path('auth/login/', auth.LoginView.as_view())
]


urlpatterns += router.urls

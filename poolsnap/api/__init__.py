from django.urls import path
from rest_framework.routers import DefaultRouter
from . import auth

router = DefaultRouter()

# router.register('login/', auth.LoginViewSet, basename='auth')

urlpatterns = [
    path('auth/login/', auth.LoginView.as_view())
]


urlpatterns += router.urls

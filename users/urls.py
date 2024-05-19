# users/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, activate_user, login_user

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/activate/<str:token>/', activate_user, name='activate_user'),
    path('users/login/<str:email>/<str:password>/<str:activation_status>/', login_user, name='login_user'),
]

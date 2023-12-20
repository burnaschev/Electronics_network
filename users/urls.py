from django.urls import path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig

app_name = UsersConfig.name

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('users/api/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
urlpatterns += users_router.urls

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProfileAPIView, UserModelViewSet

router = DefaultRouter()
router.register("", UserModelViewSet, basename="users-list")

urlpatterns = [
    path("users/", include(router.urls)),
    path("profile/", ProfileAPIView.as_view()),
    path("profile/<int:id>", ProfileAPIView.as_view()),
]

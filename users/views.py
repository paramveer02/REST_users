from django.shortcuts import render
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .mixins.views import ActionBasedModelViewSetMixin
from .models import Profile, User
from .serializers import (
    ProfileSerializer,
    UserCreateSerializer,
    UserMeSerializer,
    UserReadOnlySerializer,
)


class UserModelViewSet(ActionBasedModelViewSetMixin, ModelViewSet):
    serializer_class = UserReadOnlySerializer
    action_serializer_class = {
        "list": UserReadOnlySerializer,
        "create": UserCreateSerializer,
        "retrieve": UserMeSerializer,
    }

    def get_queryset(self):
        users = User.objects.all()
        return users


class ProfileAPIView(RetrieveUpdateAPIView, GenericAPIView):
    http_method_names = ["get", "patch", "head", "options"]
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser]
    lookup_field = "id"
    queryset = Profile.objects.all()

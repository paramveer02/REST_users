from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from pyexpat import model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Profile, User


class UserReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "dob", "name", "password"]

        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
        }

    def create(self, validated_data):
        user = User(email=validated_data["email"], dob=validated_data["dob"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_password(self, value):
        user = self.context["request"].user
        try:
            validate_password(user=user, password=value)
        except DjangoValidationError as error:
            raise ValidationError({"password": error.messages})
        return value


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "dob", "name", "city"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "image", "about"]
        # depth = 1

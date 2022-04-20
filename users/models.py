from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomManager


class User(AbstractUser):
    username = None
    name = models.CharField(verbose_name=_("name"), max_length=100, null=True)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    dob = models.DateField(verbose_name=_("Date of Birth"), blank=True, null=True)
    city = models.CharField(
        verbose_name=_("city"), max_length=100, blank=True, null=True
    )

    objects = CustomManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"User: {self.email}"

    def about(self):
        return f"User:{self.email} from {self.city}"


class Profile(models.Model):
    user = models.OneToOneField(User, max_length=100, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    about = models.FileField(upload_to="media")

    def __str__(self):
        return f"Profile:{self.user}"

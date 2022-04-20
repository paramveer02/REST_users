from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomManager(BaseUserManager):
    """
    TODO:
    """

    def create_user(self, email, password, dob, **extraKwargs):
        if not email:
            raise ValueError(_("Email is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, dob=dob, **extraKwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, dob, **extraKwargs):
        extraKwargs.setdefault("is_staff", True)
        extraKwargs.setdefault("is_superuser", True)
        extraKwargs.setdefault("is_active", True)

        if extraKwargs.get("is_staff") is not True:
            raise ValueError(_("superuser must have is_staff set to True"))
        if extraKwargs.get("is_superuser") is not True:
            raise ValueError(_("superuser must have is_superuser set to True"))
        if extraKwargs.get("is_active") is not True:
            raise ValueError(_("superuser must have is_active set to True"))
        return self.create_user(email, password, dob, **extraKwargs)

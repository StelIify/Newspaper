from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)  # blank - value required or not in the form
    email = models.EmailField(_('email address'), unique=True)

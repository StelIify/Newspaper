from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)  # blank - value required or not in the form
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(default='default.jpg', storage=OverwriteStorage(), upload_to='profile_pictures')

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


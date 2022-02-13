from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

    is_author = models.BooleanField(default=False)
    special_user = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to="images", default='../static/images/avatars/user-05.jpeg', blank=True)
    description = models.TextField(default="hi there!")

    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        else:
            return False
    is_special_user.boolean = True
    is_special_user.short_description = "Special user"
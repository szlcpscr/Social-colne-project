from django.db import models
from django.contrib import auth

# Create your models here.


class User2(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

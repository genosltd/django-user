from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

import re


class User(AbstractUser):
    def clean(self):
        username = self.username.lower()
        if not re.match(r'[a-z]+@genos.hr', username):
            raise ValidationError({'username': "Username should be your 'genos.hr' email"})

        if not self._state.adding:
            self.email = self.username

        super().clean()

    def save(self, *args, **kwargs):
        self.email = self.username
        super().save(*args, **kwargs)

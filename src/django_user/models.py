from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.conf import settings

import re
import datetime


USERNAME_REGEX = getattr(settings, 'USERNAME_REGEX', r'[a-z]+@[a-z]+.[a-z]+')


class User(AbstractUser):
    failed_logins_limit = 3
    failed_logins_period = datetime.timedelta(minutes=5)

    failed_logins_started = models.DateTimeField(editable=False, null=True)
    failed_logins_count = models.PositiveSmallIntegerField(editable=False,
                                                           default=0)

    def clean(self):
        username = self.username.lower()
        if not re.match(USERNAME_REGEX, username):
            raise ValidationError({'username':
                                   "Username should be your 'genos.hr' email"})

        if not self._state.adding:
            self.email = self.username

        super().clean()

    def save(self, *args, **kwargs):
        self.email = self.username
        super().save(*args, **kwargs)


# FIXME: not working as expected
# User.username.field.verbose_name = 'Email'

from django.contrib.auth.backends import ModelBackend as AuthModelBackend
from django.contrib.auth import PermissionDenied

from django.utils import timezone

from .models import User


class ModelBackend(AuthModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username=username,
                                    password=password, **kwargs)
        if user:
            count = user.failed_logins_count
            limit = user.failed_logins_limit

            now = timezone.now()
            started = user.failed_logins_started
            period = user.failed_logins_period

            if count >= limit and (now - started) < period:
                raise PermissionDenied

            elif count > 0:
                user.failed_logins_count = 0
                user.failed_logins_started = None
                user.save()

            return user

        else:
            user = User.objects.get(username=username)
            if user.failed_logins_count == 0:
                user.failed_logins_started = timezone.now()

            user.failed_logins_count += 1
            user.save()

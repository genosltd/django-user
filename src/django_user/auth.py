from django.contrib.auth.backends import ModelBackend as AuthModelBackend

from django.utils import timezone


class ModelBackend(AuthModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username=username,
                                    password=password, **kwargs)
        if user:
            count = user.failed_logins_count
            limit = user.failed_logins_limit

            started = user.failed_logins_started
            period = user.failed_logins_period

            if count > limit and (timezone.now() - started) < period:
                user = None

        return user

from django.contrib.auth import user_login_failed, user_logged_in
from django.dispatch import receiver
from .models import User

from django.utils import timezone


# @receiver(user_login_failed)
@receiver(user_login_failed, dispatch_uid='failed_login')
def failed_login(sender, **kwargs):
    username = kwargs['credentials']['username']
    user = User.objects.get(username=username)

    if user.failed_logins_count == 0:
        user.failed_logins_started = timezone.now()

    user.failed_logins_count += 1
    user.save()


@receiver(user_logged_in, dispatch_uid='user_login')
def user_login(sender, **kwargs):
    user = kwargs['user']
    if user.failed_logins_count > 0:
        user.failed_logins_count = 0
        user.failed_logins_started = None
        user.save()

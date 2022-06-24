from django.test import TestCase, override_settings
from django.core.exceptions import ValidationError

from django_user.models import User


@override_settings(USERNAME_REGEX=r'[a-z]+@proba.org')
class TestUser(TestCase):
    def test_save(self):
        user = User(username='proba@proba.org')
        user.save()

    def test_clean(self):
        user = User(username='proba@proba.org')
        user.clean()

    def test_clean_update(self):
        user = User(username='proba@proba.org')
        user.save()
        user.clean()

    def test_clean_fail(self):
        user = User(username='a@a.a')
        with self.assertRaisesMessage(
            ValidationError,
            f"Username should match '{user.USERNAME_REGEX}' pattern"
        ):
            user.clean()

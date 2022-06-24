from django.test import TestCase, override_settings

from django_user.models import User


@override_settings(USERNAME_REGEX=r'[a-z]+@proba.org')
class TestUser(TestCase):
    def test_save(self):
        user = User(username='proba@proba.org')
        user.save()

    def test_clean(self):
        user = User(username='proba@genos.hr')
        user.clean()

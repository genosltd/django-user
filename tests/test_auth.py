from django.test import TestCase, override_settings
from django_user.models import User


class TestAuth(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='proba@proba.org',
            password='password'
        )

    def test_authenticate(self):
        self.assertTrue(self.client.login(username='proba@proba.org',
                                          password='password'))

    def test_failed_login_over_limit(self):
        login = self.client.login
        for _ in range(self.user.failed_logins_limit):
            login(username='proba@proba.org', password='')

        self.assertFalse(login(username='proba@proba.org',
                               password='password'))

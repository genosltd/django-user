#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)

    # https://docs.djangoproject.com/en/4.0/topics/testing/advanced/#defining-a-test-runner
    test_runner = TestRunner(
        verbosity=2,
        interactive=True,
        failfast=False,
        debug_sql=False,
        pdb=True,
    )
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))

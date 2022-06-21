# Django User

## Installation

~~~
> pipenv install https://github.com/genosltd/django-user
~~~

## Usage

Do not forget to list `django-user` in `settings.py`:

~~~python
# settings.py
INSTALLED_APPS = [
    'django-user',
]
~~~

### Models

### Admin


### Testing

For testing please use:

~~~
> pipenv run tests\runtests.py
~~~

or with coverage:

~~~
> pipenv run coverage run --source django_user tests\runtests.py
~~~

and then for html coverage report (in `htmlcov`):

~~~
> pipenv run coverage html
~~~


"""
WSGI config for What project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from . import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "What.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
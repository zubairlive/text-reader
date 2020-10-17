import codecs
from os import environ

import yaml
# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

from text_reader.settings.base import *

DEBUG = False
# ------------------------------
# HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
# END HOST CONFIGURATION
# ------------------------------

LOGGING['handlers']['local']['level'] = 'INFO'

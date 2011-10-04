import os
import sys

APP_DIR = os.path.dirname(__file__)

sys.path.insert(0, APP_DIR)
sys.path.insert(0, APP_DIR + '/salesevents')

os.environ['DJANGO_SETTINGS_MODULE'] = 'salesevents.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import os, sys
sys.path.append('/var/www/django')
sys.path.append('/var/www/django/sportsshop')
os.environ['DJANGO_SETTINGS_MODULE'] = 'sportsshop.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

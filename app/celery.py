from __future__ import absolute_import
import os
from celery import Celery

# from core_app.settings import INSTALLED_APPS
# from core_app.core_app.settings import INSTALLED_APPS

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
from django.conf.global_settings import INSTALLED_APPS

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_app.settings')

# you change the name here
app = Celery("app")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks()

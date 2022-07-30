from celery import shared_task
from datetime import datetime
from time import sleep

from .utils import GoogleSheets, get_usd_currency
from .models import Order


@shared_task
def run():
    pass

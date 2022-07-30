from django.core.management import BaseCommand
from datetime import datetime
from time import sleep

from ...utils import GoogleSheets, get_usd_currency
from ...models import Order


class Command(BaseCommand):
    help = 'Эта команда запускает работу программы'

    def handle(self, *args, **kwargs):
        g = GoogleSheets()

        while True:
            data = g.get_value()
            currency_datetime = datetime.now()
            for el in data:
                try:
                    order = Order.objects.get(order=el[0])
                    if order.usd_cost != el[1] or order.delivery_time != el[2]:
                        order.usd_cost = el[1]
                        order.delivery_time = el[2]
                        usd_rub = get_usd_currency(el[2])
                        if usd_rub.get('status') == 'ok':
                            order.rub_cost = int(el[1]) * usd_rub.get('value')
                    order.updated = currency_datetime
                    order.save()
                except Order.DoesNotExist:
                    Order.objects.create(order=el[0],
                                         usd_cost=el[1],
                                         delivery_time=el[2],
                                         rub_cost=int(el[1]) * usd_rub.get('value'),
                                         updated=currency_datetime
                                         )

            Order.objects.exclude(updated=currency_datetime).delete()
            print('Wait 1 sec')
            sleep(1)

from django.db import models


class Order(models.Model):
    """
    Данные заказа
    """
    order = models.IntegerField()
    usd_cost = models.IntegerField()
    delivery_time = models.CharField(max_length=64)
    rub_cost = models.DecimalField(max_digits=15, decimal_places=4, null=True)
    updated = models.DateTimeField(null=True)


class Currency(models.Model):
    """
    Хранит курс доллар-рубль на определнную дату
    """
    date = models.CharField(max_length=64, null=True)
    usd_rub = models.DecimalField(max_digits=7, decimal_places=4, null=True)


class Subscriber(models.Model):
    """
    ПОдписчики на сообщения телеграм бота
    """
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=128)
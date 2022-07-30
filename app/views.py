from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer

from .tasks import run


def index(request):
    """
    Запускаем задачу при входе на главную страницу
    :param request:
    :return:
    """
    print('Start tasks')
    result = run.delay()
    return render(request, 'index.html', {'telegram_bot': 'https://tglink.ru/simple_heroku_bot'})


class OrderApiListView(APIView):
    """
    Возвращает список всех заказов
    """
    def get(self, request, format=None):
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

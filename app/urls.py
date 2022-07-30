from django.urls import path

from .views import index, OrderApiListView


urlpatterns = [
    path('', index),
    path('api/v1/orders/', OrderApiListView.as_view()),
]
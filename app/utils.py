import requests
from bs4 import BeautifulSoup

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

import environ
import os

from .models import Currency

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


def get_usd_currency(date: str):
    """
    Получает курс доллара на определенную дату
    :param date: 01.01.2022
    :return: {'status': 'ok', 'value': 50.4322}
    """
    try:
        currency = Currency.objects.get(date=date)
        return {'status': 'ok',
                'value': currency.usd_rub}
    except Currency.DoesNotExist:
        pass

    date_req = date.replace('.', '/')
    params = {'date_req': date_req}
    url = 'https://www.cbr.ru/scripts/XML_daily.asp'
    try:
        req = requests.get(url=url, params=params)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'lxml')
            value = float(soup.find('valute', {'id': 'R01235'}).find('value').text.replace(',', '.'))
            Currency.objects.create(date=date,
                                    usd_rub=value)
            return {'status': 'ok',
                    'value': value}
        else:
            return {'status': 'error'}
    except Exception as e:
        return {'status': 'error',
                'detail': e}


class GoogleSheets:
    def __init__(self):
        self.CREDENTIALS_FILE = os.path.join(BASE_DIR,
                                             'creds.json')
        self.spreadsheet_id = env('SPREADSHEET_ID')

        # Читаем ключи из файла
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            self.CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])

        self.httpAuth = self.credentials.authorize(httplib2.Http())  # Авторизуемся в системе
        self.service = apiclient.discovery.build('sheets', 'v4',
                                                 http=self.httpAuth)  # Выбираем работу с таблицами и 4 версию API

    def get_value(self):
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range='B2:D60',
            majorDimension='ROWS'
        ).execute()
        return values.get('values')

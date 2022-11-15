from __future__ import absolute_import, unicode_literals
from celery import shared_task
from typing import Callable

from bs4 import BeautifulSoup
import urllib.request
import json

# Cache handling
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT  # 300s

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@shared_task
def get_world_stock_from_stooq_pl() -> json:
    """
    Function scraps stooq.pl website for world stock data and
    caches it to Redis
    Returns:
        json: {ID_x: {'Name': "", 'Value': "", 'Change': "", 'Date': ""},}
    """
    url = "https://static.stooq.com/pp/w.js"
    page = urllib.request.urlopen(url)
    tree = BeautifulSoup(page, 'html.parser')
    table = tree.find('table')
    table_columns = table.find_all('tr')
    stock_data = {}
    stock_keys = ['Name', 'Value', 'Change', 'Date']

    # Serialize date to specific columns without table tittle
    for i, col in enumerate(table_columns[1:]):
        data = col.find_all('td')
        if len(data) == 0:
            continue

        # single stock dict creation
        single_stock_data = {}
        for idx, key in enumerate(stock_keys):
            value = data[idx].getText()
            single_stock_data[key] = value

        # append single stock to stock dict
        stock_key = f'ID_{i+1}'
        stock_data[stock_key] = single_stock_data

    json_data = json.dumps(stock_data)
    cache.set("Data", json_data)

    return json_data


# def save_data_to_csv(data: list[str], name: str) -> None:
#     with open(f'{name}.csv', 'w', newline='') as file:
#         csv_output = csv.writer(file)
#         csv_output.writerows(data)

# @shared_task
# def save_world_stock_from_stooq_pl_csv():

#     url = "https://static.stooq.com/pp/w.js"
#     page = urllib.request.urlopen(url)
#     tree = BeautifulSoup(page, 'html.parser')
#     table = tree.find('table')
#     table_columns = table.find_all('tr')
#     stock_data = []
#     stock_data.append(['Name', 'Value', 'Change', 'Date'])

#     # Serialize date to specific columns without table tittle
#     for col in table_columns[1:]:
#         data = col.find_all('td')
#         if len(data) == 0:
#             continue
#         name = data[0].getText()
#         value = data[1].getText()
#         change = data[2].getText()
#         date = data[3].getText()
#         stock_data.append([name, value, change, date])
#     save_data_to_csv(stock_data, "world_stock")

#     return stock_data

# @shared_task
# def check_result(func: Callable, *args, **kwargs) -> None:
#     result = func.delay(*args, **kwargs)
#     if result.ready():
#         print("Task has run")
#         if result.successful():
#             print("Result was: %s" % result.result)
#         else:
#             if isinstance(result.result, Exception):
#                 print("Task failed due to raising an exception")
#                 raise result.result
#             else:
#                 print("Task failed without raising an exception")
#     else:
#         print("Task has not yet run")

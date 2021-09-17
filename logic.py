import requests
from requests.structures import CaseInsensitiveDict
from datetime import datetime, timedelta
from login import headers


class Getters:
    """
    Include objects with request.get

    :method response: Return result of request.get in JSON
    """
    def __init__(self, request_link, params, head=headers):
        """
        :param request_link: Link for request, str
        :param params: parameters of get request, str
        :param head: headers of get requests, CaseInsensitiveDict
        """
        if isinstance(request_link, str):
            self.link = request_link
        else:
            raise ValueError('Link must be a string')
        if isinstance(headers, requests.structures.CaseInsensitiveDict):
            self.headers = head
        else:
            raise ValueError('Headers must be a dict')
        if isinstance(params, str) or params is None:
            self.params = params
        else:
            raise ValueError('Params must be a string')

    def response(self):
        """
        :return: response in JSON format
        """
        response = requests.get(self.link + self.params,
                                headers=self.headers)
        return response.json()


def get_cost_param(quantity=1):
    """
    Create parameters string to get_cost obj
    :param quantity:  0 - all, 1 - not null quantity, 2 - null quantity
    :return: parameter string
    """
    param = ''
    QUANTITY_LIST = [1, 2, 0]
    if quantity not in QUANTITY_LIST:
        raise ValueError('Quantity must be 1, 2 or 0')
    else:
        param.join(f'quantity={quantity}')
    return param


url_cost = f"https://suppliers-api.wildberries.ru/public/api/v1/info"


def get_market_param(search=None, skip=0, take=10, sort=None,
                     order=None):
    """
    Create parameters string for
    :param search: None or str
           Word or word fragment to search
    :param skip: int
           How much strings to skip (pagination)
    :param take: int
           How much strings to take (pagination)
    :param sort: None or name of field to sort str(subject,
                 brand, name, size, barcode, articles)
           On which field sort
    :param order: None or str(asc) or str(desc)
    :return: str
            parameters for get_stocks
    """
    param = '?'
    RIGHT_SORT_LIST = ['subject', 'brand', 'name', 'size',
                       'barcode', 'articles']
    ORDER_LIST = ['asc', 'desc']
    if isinstance(search, str):
        param += ''.join(f'search={search}&')
    elif not isinstance(search, str) and search is not None:
        raise ValueError("search must be a str")
    if not isinstance(skip, int):
        raise ValueError('skip must be an int')
    if not isinstance(take, int):
        raise ValueError('take must be an int')
    param += ''.join(f'skip={skip}&take={take}')
    if sort in RIGHT_SORT_LIST:
        param += ''.join(f'&sort={sort}')
    elif sort is not None and sort not in RIGHT_SORT_LIST:
        raise ValueError("sort must be subject, brand, name,"
                         "size, barcode or articles")
    if order in ORDER_LIST:
        param += ''.join(f'&order={order}')
    elif order is not None and order not in ORDER_LIST:
        raise ValueError("order must be asc or desc")
    return param


marketplace_url = "https://suppliers-api.wildberries.ru/api/v2/stocks"

warehouse_url = "https://suppliers-api.wildberries.ru/api/v2/warehouses"


def get_orders_param(date_start=(datetime.today() - timedelta(days=1)),
                     date_end=None, status=None, take=10, skip=0,
                     order_id=None):
    param ='?'
    STATUSES_LIST = list(range(0, 8))
    date_format = '%Y-%m-%dT'  # formatting time into RFC3339
    if not isinstance(date_start, datetime):
        raise ValueError("date_start must be datetime obj")
    date_start = date_start.strftime(date_format)
    param += ''.join(f'date_start={date_start}' +
                     '00%3A00%3A00.000%2B10%3A00')
    if isinstance(date_end, datetime):
        date_end = date_end.strftime(date_format)
        param += ''.join(f'&date_end={date_end}' +
                         '00%3A00%3A00.000%2B10%3A00')
    elif date_end is not None and not isinstance(date_end, datetime):
        raise ValueError('date_end must be datetime obj')
    if isinstance(status, int):
        param += ''.join(f'&status={status}')
    elif status is not None and status not in STATUSES_LIST:
        raise ValueError('status must be int in range from 0 to 7')
    if not isinstance(take, int):
        raise ValueError('take must be an int')
    if not isinstance(skip, int):
        raise ValueError('skip must be an int')
    param += ''.join(f'&skip={skip}&take={take}')
    if isinstance(order_id, int):
        param += ''.join(f'&id={order_id}')
    elif order_id is not None and not isinstance(order_id, int):
        raise ValueError('order_id must be an int')
    print(param)
    return param


orders_url = 'https://suppliers-api.wildberries.ru/api/v2/orders'

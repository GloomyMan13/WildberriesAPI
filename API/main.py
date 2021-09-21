from API.logic import Getters, GetObjectInfo
from API.login import headers

orders = 'search by pattern'
get_orders = GetObjectInfo(orders, headers, name='Шампуни', parent='Красота')
print(get_orders.response())


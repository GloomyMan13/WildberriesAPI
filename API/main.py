from API.logic import Getters, GetObjectInfo
from API.login import headers

orders = 'config'
get_orders = GetObjectInfo(orders, headers, name='Шампуни')
print(get_orders.response())


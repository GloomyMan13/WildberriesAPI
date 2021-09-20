from API.logic import Getters
from API.login import headers

orders = 'stocks'
get_orders = Getters(orders, head=headers, take=20)


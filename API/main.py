from logic import Getters
from login import headers

orders = 'stocks'
get_orders = Getters(orders, head=headers, take=20)


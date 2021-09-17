from logic import Getters, url_cost, get_cost_param, marketplace_url,\
    get_market_param, warehouse_url, orders_url, get_orders_param

get_costs = Getters(url_cost, get_cost_param())
get_stocks = Getters(marketplace_url, get_market_param())
warehouse = Getters(warehouse_url, None)
get_orders = Getters(orders_url, get_orders_param())
print(get_orders.response())

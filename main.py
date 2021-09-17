from logic import Getters

def cost_param(quanity=1):
    param = ''
    QUANITY_LIST = [1, 2, 0]
    if quanity not in QUANITY_LIST:
        raise ValueError('Quanity must be 1, 2 or 0')
    else:
        param.join(f'quanity={quanity}')
    return param


url_cost = f"https://suppliers-api.wildberries.ru/public/api/v1/info"
costs = Getters(url_cost, cost_param())


def market_param(search=None, skip='0', take='10', sort=None, order=None):
    param = '?'
    RIGHT_SORT_LIST = ['subject', 'brand', 'name', 'size', 'barcode', 'articles']
    ORDER_LIST = ['asc', 'desc']

    if search is not None and isinstance(search, str):
        param += ''.join(f'search={search}&')
    elif search is not None and not isinstance(search, str):
        raise ValueError("Param search must be a str")
    param += ''.join(f'skip={skip}&')
    param += ''.join(f'take={take}')
    if sort is not None and sort in RIGHT_SORT_LIST:
        param += ''.join(f'&sort={sort}')
    elif sort is not None and sort not in RIGHT_SORT_LIST:
        raise ValueError("Param sort must be subject, brand, name, size, barcode or articles")
    if order is not None and order in ORDER_LIST:
        param += ''.join(f'&order={order}')
    elif order is not None and order not in ORDER_LIST:
        raise ValueError("Param order must be asc or desc")
    return param


marketplace_url = "https://suppliers-api.wildberries.ru/api/v2/stocks"
stocks = Getters(marketplace_url, market_param())
print(stocks.responce())

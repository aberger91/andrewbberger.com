from .oanda_fx_api import Account, GetCandles
import requests

def converter(base, term, amount):
    acc = Account()
    pair = '%s_%s' % (base, term)
    prices = GetCandles(acc, pair, count=1).request()

    if not prices:
        pair = '%s_%s' % (term, base)
        prices = GetCandles(acc, pair, count=1).request()

    if not prices:
        return 'Invalid currency %s_%s' (base, term)

    try:
        mid = (prices[0]['closeBid'] + prices[0]['closeAsk']) / 2.0
        if term == pair[-3:]:
            rate = mid * amount
        elif term == pair[:3]:
            rate = amount / mid
    except Exception as e:
        return e

    return round(rate, 2)

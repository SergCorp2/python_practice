import json
import requests
from conf import keys

class CnvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        #values = message.text.split(' ')
        if quote == base:
            raise CnvertionException(f'невозможно провести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise CnvertionException(f'не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise CnvertionException(f'не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise CnvertionException(f'не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
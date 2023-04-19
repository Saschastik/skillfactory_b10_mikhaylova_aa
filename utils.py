import json
import requests
from config import keys


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote.lower() == base.lower():
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_tiker = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_tiker = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tiker}&tsyms={base_tiker}')
        thus = json.loads(r.content)
        total_base = thus[base_tiker] * float(amount)
        return round(total_base)

import requests
import json
from config import exchanges

class ConvertionException(Exception):
    pass

class CryptoConverer:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Не удалось перевести одинаковые валюты {base}.')

        try:
            quote_ticker = exchanges[quote]
        except KeyError:
            raise ConvertionException(f'Не удалорсь обработать валюту {quote}')

        try:
            base_ticker = exchanges[base]
        except KeyError:
            raise ConvertionException(f'Не удалорсь обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[exchanges[base]]

        return total_base
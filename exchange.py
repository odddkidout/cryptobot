import ccxt

class Exchange:
    def __init__(self, exchange_name):
        self.exchange_name = exchange_name
        self.exchange = getattr(ccxt, exchange_name)()

    def get_exchange(self):
        return self.exchange

    def get_exchange_name(self):
        return self.exchange_name

    def get_exchange_markets(self):
        return self.exchange.load_markets()
import ccxt

class Binance(ccxt.binance):
    def __init__(self, config=...):
        super().__init__(config=config)
        self.apiKey = config['apiKey']
        self.secret = config['secret']

    def fetch
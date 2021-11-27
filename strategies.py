
class strategy:
    def __init__(self, strategy):
        self.strategy = strategy    
        self.name = ""
        self.pairlist = []
        self.exchangelist = []
        self.timeframe = ""
        self.trailingStopLossBool = False
        
    def updateData(self, data):
        self.data = data

    def long(self, pair, price, amount, exchange):
        self.pair = pair
        self.price = price
        self.amount = amount
        self.exchange = exchange
        self.buy()
    
    def short(self, pair, price, amount, exchange):
        self.pair = pair
        self.price = price
        self.amount = amount
        self.exchange = exchange
        self.sell()

    def refreshIndicators(self):
        pass

    def trailingStopLoss(self, trailingStopLoss):
        self.trailingStopLoss = trailingStopLoss

    def log(self, ):
        pass

    def plot(self, ):
        pass
    
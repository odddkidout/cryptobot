from art import text2art
from configuration import configuration
import ccxt
import fastparquet
import pandas

class helper:
    def __init__(self):
        pathToConfig = "./config"
        pathToStrategy = "./strategy"
    
    @staticmethod
    def Logo():
        return text2art("CRYPTODDBOT")
    
    @staticmethod
    def Menu():
        return(" 1. Check running Task\n 2. Run Task\n 3. Make config\n 4. Backtesting\n 5. Exchange settings\n 6. Update\n 7. Plot \n 8. Download data\n 9. Fetch Market Sentiment(fear/greed)\n 10. Exit")
    
    @staticmethod
    def makeConfig():
        config = configuration()
        config.makeConfig()

    @staticmethod
    def FetchStrategies(): #fetch all strategies
        output = ""
        counter = 1
        for file in os.listdir(helper.pathToStrategy):
            if file.endswith(".py"):
                output.append(str(counter) + ". " + file[:-3])
        return output

    @staticmethod
    def downloadData():
        
        exchangeinput = input("Exchange[binance]: ")
        try:
            exchange = getattr(ccxt, exchangeinput)()
        except:
            print("Error")
            return
        """print all the pairs supported by exchange"""
        exchange.load_markets()
        print(exchange.symbols)
        pair = input("Crypto Pair: ")
        
        timeframe = input("Timeframe('1m', '5m','15m', '30m','1h', '2h', '3h', '4h', '6h', '12h', '1d', '1M', '1y'):\n ")

        print("Exchange :{} \nPair : {}\nTimeframe : {}" .format(exchange, pair, timeframe))
        print("Downloading data...")

        
        """check if timeframe is available on exchange if not return a helpful error"""
        
        if timeframe not in exchange.timeframes:
            print('{} does not support {} timeframe. Please use another timeframe'
            .format(exchange.name, timeframe))
            return

        """check if crypto pair is available on exchange"""
        
        if pair not in exchange.symbols:
            print('{} does not support {} crypto pair. Please use another crypto pair'
            .format(exchange.name, pair))
            return

        """check if exchange supports fetching OHLCV data"""
        
        if exchange.has["fetchOHLCV"] != True:
            print('{} does not support fetching OHLC data. Please use another exchange'
            .format(exchange.name))
            return
        
        """get data"""
        
        data = exchange.fetch_ohlcv(pair, timeframe)
        
        """save data to parq file"""
        header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
        pairs = pair.split('/')
        fastparquet.write("./data/{}-{}_{}.parq".format(pairs[0],pairs[1], timeframe),pandas.DataFrame(data, columns=header).set_index('Timestamp'), compression='gzip')
        print("Data saved to ./data/{}_{}.parq".format(pair, timeframe))

from art import text2art
from configuration import configuration

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
        print("Downloading data...")



        

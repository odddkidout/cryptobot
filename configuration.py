import json
import os

from constants import helper

class configuration:
    def __init__(self):
        self.path_to_config = "./config/{name}.json"
        self.path_to_log = "./config/log.txt"
        self.name = "" # name of the Configuration
        self.strategycode = "" # strategy code
        self.pairlist = [] # list of pairs
        self.exchangelist = []  # list of exchange names
        self.demomode = True # True = Demo, False = Live
        self.debugmode = False      
        self.verbosemode = False  # verbose mode is not implemented yet
        self.loggingmode = False  # Logging to file
        self.usingApi = False  # True if using API
        self.signalApiKey = ""  # API key for signal
        self.discord = False  # True if using discord
        self.discord_webhook = ""  # Webhook for discord
        self.telegram = False  # True if using telegram
        self.telegram_bot_token = ""  # Token for telegram bot
        self.telegram_chat_id = ""  # Chat ID for telegram
        self.telegram_bot_name = ""  # Bot name for telegram
    
    def makeConfig(self):
        while(self.name.isspace()):
            self.name = input("Enter a name for the configuration: ") 
        self.strategycode = input(helper.FetchStrategies())    
        self.name = input("Please enter the name of the configuration: ")
        if name.isspace():
            print("Name cannot be empty!")
        self.strategycode = input("Please enter the strategy code: ")
        self.pairlist = input("Please enter the pairs you want to trade: ")
        self.exchangelist = input("Please enter the exchanges you want to trade on: ")
        self.demomode = input("Demo mode? (y/n): ")
        self.debugmode = input("Debug mode? (y/n): ")
        self.verbosemode = input("Verbose mode? (y/n): ")
        self.loggingmode = input("Logging to file? (y/n): ")
        self.usingApi = input("Using API? (y/n): ")
        self.signalApiKey = input("API key for signal: ")
        self.discord = input("Using discord? (y/n): ")
        self.discord_webhook = input("Webhook for discord: ")
        self.telegram = input("Using telegram? (y/n): ")
        self.telegram_bot_token = input("Token for telegram bot: ")
        self.telegram_chat_id = input("Chat ID for telegram: ")
        self.telegram_bot_name = input("Bot name for telegram: ")
        self.save()

    def fromJson(self, json_string):
        self.__dict__ = json.loads(json_string)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        
    def save(self):
        if not os.path.exists("./config"):
            os.makedirs("./config")
        with open(self.path_to_config.format(name=self.name), "w") as f:
            f.write(self.toJson())
        if self.loggingmode:
            with open(self.path_to_log, "w") as f:
                f.write(self.toJson())

    def print(self):
        print(self.toJson())    
    
    def load(self, name):
        self.name = name
        with open(self.path_to_config.format(name=self.name), "r") as f:
            self.fromJson(f.read())
        if self.loggingmode:
            with open(self.path_to_log, "r") as f:
                self.fromJson(f.read())
        return self
    
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import indicators
import asyncio
"""
    inputs: pair of cryptocurrency, timeframe, strategy(optional), indicator(optional)

"""
class plot:
    def __init__(self, pair, timeframe, strategy=None, indicator=None, data = None):
        self.pair = pair
        self.timeframe = timeframe
        if data is None:
            self.read_data_parquet()
        self.fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05,subplot_titles=('OHLC', 'Volume'),
            row_width=[0.2, 0.7])
        self.fig.update_layout(
            title_text="Candlestick Graph",
            xaxis_title_text="Date",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )
        )

    def plot_candlestick(self):
        print(self.data.index.values)
        self.fig.add_trace(go.Candlestick(x=self.data.index.values, open=self.data["Open"], high=self.data["Close"],
                low=self.data["Low"], close=self.data["Close"], name="OHLC"), 
                row=1, col=1)
        self.fig.update_xaxes(title_text="Date", row=1, col=1)
        self.fig.update_yaxes(title_text="Prices", row=1, col=1)

    def plot_volume(self):
        self.fig.add_trace(go.Bar(x=self.data.index.values, y=self.data["Volume"], name="Volume"), row=2, col=1)
        self.fig.update_xaxes(title_text="Date", row=2, col=1)
        self.fig.update_yaxes(title_text="Volume", row=2, col=1)
        
    def plot_indicators(self, datadown,dataup,ma):
        """plot a line"""
        self.fig.add_trace(go.Scatter(x=self.data.index.values, y=datadown, name="SSL down",line_color='#FF0000'), row=1, col=1)
        self.fig.add_trace(go.Scatter(x=self.data.index.values, y=dataup, name="SSL up",line_color='#00FF00'), row=1, col=1)
        self.fig.add_trace(go.Scatter(x=self.data.index.values, y=ma, name="MA",line_color='#FFFF00'), row=1, col=1)
    


    def show(self):
        self.fig.show()

    def read_data_parquet(self):
        pairs = self.pair.split("/")
        path = "./data/{}-{}_{}.parq".format(pairs[0],pairs[1], self.timeframe)
        self.data = pd.read_parquet(path)
        print(self.data)
        
plot = plot("BTC/USDT", "30m")
plot.plot_candlestick()
plot.plot_volume()
loop = asyncio.get_event_loop()
tasks = indicators.SSLChannels(plot.data), indicators.MovingAverage(plot.data,0)
ssl,ma = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
plot.plot_indicators(ssl["sslDown"],ssl["sslUp"],ma)
plot.show()
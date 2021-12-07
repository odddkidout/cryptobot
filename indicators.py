import pandas as pd
import numpy as np
import asyncio
@asyncio.coroutine
async def SSLChannels(dataframe, length=10, mode="sma"):
    """
    Source: https://www.tradingview.com/script/xzIoaIJC-SSL-channel/
    Author: xmatthias
    Pinescript Author: ErwinBeckers
    SSL Channels.
    Average over highs and lows form a channel - lines "flip" when close crosses
    either of the 2 lines.
    Trading ideas:
        * Channel cross
        * as confirmation based on up > down for long
    Usage:
        dataframe['sslDown'], dataframe['sslUp'] = SSLChannels(dataframe, 10)
    """
    if mode not in ("sma"):
        raise ValueError(f"Mode {mode} not supported yet")

    df = dataframe.copy()

    if mode == "sma":
        df["smaHigh"] = df["High"].rolling(20).mean()
        df["smaLow"] = df["Low"].rolling(20).mean()

    df["hlv"] = np.where(
        df["Close"] > df["smaHigh"], 1, np.where(df["Close"] < df["smaLow"], -1, np.NAN)
    )
    df["hlv"] = df["hlv"].ffill()

    df["sslDown"] = np.where(df["hlv"] < 0, df["smaHigh"], df["smaLow"])
    df["sslUp"] = np.where(df["hlv"] < 0, df["smaLow"], df["smaHigh"])
    return df
    return df["sslDown"], df["sslUp"]
@asyncio.coroutine
async def MovingAverage(dataframe, mode, length=21):

    """return moving average of lenght lenght of different type"""

    if mode > -1 & mode <4:
        raise ValueError(f"Mode {mode} not supported yet")

    df = dataframe.copy()

    if mode == 0:
        ma = df["Close"].rolling(length).mean()
    elif mode == 1:
        ma = df["Close"].ewm(span=length).mean()
    elif mode == 2:
        """smoothed moving average"""

    elif mode == 3:
        """linear weighted moving average"""
    return ma
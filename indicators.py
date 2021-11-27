import pandas as pd
import numpy as np


def SSLChannels(dataframe, length=10, mode="sma"):
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
        df["smaHigh"] = df["high"].rolling(length).mean()
        df["smaLow"] = df["low"].rolling(length).mean()

    df["hlv"] = np.where(
        df["close"] > df["smaHigh"], 1, np.where(df["close"] < df["smaLow"], -1, np.NAN)
    )
    df["hlv"] = df["hlv"].ffill()

    df["sslDown"] = np.where(df["hlv"] < 0, df["smaHigh"], df["smaLow"])
    df["sslUp"] = np.where(df["hlv"] < 0, df["smaLow"], df["smaHigh"])

    return df["sslDown"], df["sslUp"]
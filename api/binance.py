import requests
import pandas as pd
import time

from helpers.functions import count_time_from_2010, TimeFrame, Symbols


def get_binance_historical_data(symbol=Symbols, interval=TimeFrame):
    url = "https://api.binance.com/api/v3/klines"
    total_candles = []
    end_time = None
    limit = count_time_from_2010(interval.value['seconds'])

    while len(total_candles) < limit:
        params = {
            "symbol": symbol.value,
            "interval": interval.value['api_interval'],
            "limit": min(1000, limit - len(total_candles)),
        }

        if end_time:
            params["endTime"] = end_time
        print(params)
        response = requests.get(url, params=params)
        data = response.json()

        if not data:
            break

        total_candles.extend(data)


        end_time = data[-1][0] - 1

        time.sleep(1)


    df = pd.DataFrame(total_candles, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "trades",
        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])


    df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)

    return df[["timestamp", "open", "high", "low", "close", "volume"]]

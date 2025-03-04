import pandas as pd

from api.binance import get_binance_historical_data
from helpers.functions import TimeFrame, Symbols
import os.path

latest_btc = None
if os.path.isfile('data/btc_1h.csv'):
    latest_btc = pd.read_csv('data/btc_1h.csv')
    btc = get_binance_historical_data(symbol=Symbols.BTCUSDT, interval=TimeFrame.ONE_HOUR, last_candle=int(latest_btc.iloc[-1,1]))
    result = pd.concat([btc, latest_btc]) if not btc.empty else latest_btc
    result = result.sort_values(by=['timestamp'])
else:
    result = get_binance_historical_data(symbol=Symbols.BTCUSDT, interval=TimeFrame.ONE_HOUR)
if len(result.index)>0:
    result = result.drop_duplicates(subset=['timestamp'])
    result.to_csv('data/btc_1h.csv', index=False)

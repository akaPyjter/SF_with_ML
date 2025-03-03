import pandas as pd

from api.binance import get_binance_historical_data
from helpers.functions import TimeFrame, Symbols

btc = get_binance_historical_data(symbol=Symbols.BTCUSDT, interval=TimeFrame.ONE_HOUR)
btc.to_csv('data/btc_1h.csv')
# btc = pd.read_csv('data/btc_1h.csv')
# btc['avg'] = btc[['high', 'low']].mean(axis=1)
# print(btc)

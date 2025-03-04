import pandas as pd



def filter_hammers(dataset: pd.DataFrame)-> pd.DataFrame:
    columns = dataset.columns
    print(columns)
    row_list = []
    for row in dataset.itertuples(index=False):
        timestamp, open_, high, low, close, volume = row
        candle_width = abs(open_ - close)
        high_width = high - open_ if high - open_ < high - close else high - close
        shadow = high - candle_width - candle_width

        if shadow >= candle_width  and high_width < 0.5 * candle_width:
            temp_dict = {
                columns[0] : timestamp,
                columns[1]: open_,
                columns[2]: high,
                columns[3]: low,
                columns[4]: close,
                columns[5]: volume,
            }
            row_list.append(temp_dict)
    return pd.DataFrame(row_list)


data = pd.DataFrame(columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
data.loc[-1] = [0, 15, 20, 10, 19,1 ]
print(len(filter_hammers(data)))


print(len(filter_hammers(pd.read_csv('../data/btc_1h.csv'))))
print(len(pd.read_csv('../data/btc_1h.csv')))
import pandas as pd



def filter_hammers(dataset: pd.DataFrame)-> pd.DataFrame:
    columns = dataset.columns
    row_list = []
    for row in dataset.itertuples(index=False):
        timestamp, open_, high, low, close, volume = row
        candle_width = abs(open_ - close)
        lower_shadow = open_ - low if open_ > close else close - low
        upper_shadow = high - max(open_, close)
        if lower_shadow >= candle_width * 2 and upper_shadow <= candle_width * 0.2:
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




print(len(filter_hammers(pd.read_csv('../data/btc_1h.csv'))))
print(len(pd.read_csv('../data/btc_1h.csv')))
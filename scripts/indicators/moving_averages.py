import talib

def add_moving_averages(df, short_window=20, long_window=50):
    df['SMA20'] = talib.SMA(df['close'], timeperiod=short_window)
    df['SMA50'] = talib.SMA(df['close'], timeperiod=long_window)
    return df

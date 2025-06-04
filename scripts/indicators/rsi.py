import talib

def add_rsi(df, period=14):
    df['RSI'] = talib.RSI(df['close'], timeperiod=period)
    return df

import talib

def add_macd(df):
    macd, signal, hist = talib.MACD(df['close'])
    df['MACD'] = macd
    df['MACD_signal'] = signal
    df['MACD_hist'] = hist
    return df

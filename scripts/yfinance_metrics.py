import yfinance as yf
import pandas as pd

def get_returns(ticker, start="2023-01-01", end="2024-01-01"):
    try:
        df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
        df = df.dropna()
        returns = df['Close'].pct_change().dropna()
        returns_df = returns.reset_index()
        returns_df.columns = ['date', 'returns']
        return returns_df
    except Exception as e:
        print(f"Error fetching returns for {ticker}: {e}")
        return pd.DataFrame(columns=['date', 'returns'])

def get_rolling_volatility(ticker, window=20, start="2023-01-01", end="2024-01-01"):
    try:
        df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
        df = df.dropna()
        returns = df['Close'].pct_change().dropna()
        volatility = returns.rolling(window=window).std()
        vol_df = volatility.reset_index()
        vol_df.columns = ['date', 'volatility']
        return vol_df
    except Exception as e:
        print(f"Error calculating volatility for {ticker}: {e}")
        return pd.DataFrame(columns=['date', 'volatility'])

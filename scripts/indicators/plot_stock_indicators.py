import matplotlib.pyplot as plt

def plot_price_with_indicators(df, title="Stock Price with Indicators"):
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['close'], label='Close')
    if 'SMA20' in df: plt.plot(df['date'], df['SMA20'], label='SMA20')
    if 'SMA50' in df: plt.plot(df['date'], df['SMA50'], label='SMA50')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.show()

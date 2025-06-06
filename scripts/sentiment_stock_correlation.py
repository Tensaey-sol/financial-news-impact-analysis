from scipy.stats import pearsonr
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def load_stock_data(ticker, stock_data_dir="../data"):
    path = os.path.join(stock_data_dir, f"{ticker}_historical_data.csv")
    df = pd.read_csv(path, parse_dates=["Date"])
    df = df[["Date", "Close"]].rename(columns={"Date": "date_only", "Close": "stock_close"})
    df["returns"] = df["stock_close"].pct_change()
    return df

def compute_sentiment_correlation(news_df, stock_df, stock_symbol):
    # Filter sentiment for a single stock
    df_sentiment = news_df[news_df["stock"] == stock_symbol].copy()

    # Compute daily average sentiment
    df_sentiment = news_df[news_df["stock"] == stock_symbol].copy()
    daily_sentiment = df_sentiment.groupby("date_only")["compound"].mean().reset_index(name="avg_sentiment")

    # Merge sentiment and returns on date
    merged = pd.merge(daily_sentiment, stock_df, on="date_only", how="inner").dropna(subset=["avg_sentiment", "returns"])

    # Correlation and plot
    if len(merged) >= 2:
        corr, pval = pearsonr(merged["avg_sentiment"], merged["returns"])
        print(f"[{stock_symbol}] Correlation between sentiment and daily returns: {corr:.4f} (p={pval:.4f})")

        sns.regplot(x="avg_sentiment", y="returns", data=merged)
        plt.title(f"{stock_symbol}: Sentiment vs. Daily Returns")
        plt.xlabel("Average Sentiment (Compound)")
        plt.ylabel("Daily Return")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        corr, pval = None, None
        print(f"[{stock_symbol}] Not enough data to compute correlation.")

    return merged, corr, pval

def plot_correlation_bar(corr_df):
    tickers = corr_df["Stock"].unique()
    cmap = plt.cm.get_cmap('coolwarm', len(tickers))
    color_dict = {stock: cmap(i) for i, stock in enumerate(tickers)}
    
    plt.figure(figsize=(8, 5))
    ax = sns.barplot(
        x="Stock",
        y="Correlation",
        data=corr_df,
        color='gray'
    )
    
    for i, bar in enumerate(ax.patches):
        stock = corr_df.iloc[i]["Stock"]
        bar.set_color(color_dict.get(stock, '#333333'))
    
    plt.axhline(0, color='gray', linestyle='--')
    for i, v in enumerate(corr_df["Correlation"]):
        plt.text(i, v, f"{v:.2f}", ha='center', va='bottom' if v > 0 else 'top', fontsize=10)
    plt.title("Correlation: Daily Sentiment vs Daily Return (per Stock)")
    plt.ylabel("Pearson Correlation")
    plt.xlabel("Stock")
    plt.tight_layout()
    plt.show()
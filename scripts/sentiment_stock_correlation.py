import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import os

def load_stock_data(ticker, stock_data_dir="../data"):
    stock_path = os.path.join(stock_data_dir, f"{ticker}_historical_data.csv")
    stock_df = pd.read_csv(stock_path, parse_dates=["Date"])
    stock_df = stock_df[["Date", "Close"]].rename(columns={"Date": "date_only", "Close": "stock_close"})
    return stock_df

def compute_sentiment_correlation(news_df, stock_df, stock_symbol):
    sentiment_daily = news_df[news_df["stock"] == stock_symbol]
    sentiment_daily = sentiment_daily.groupby("date_only")["compound"].mean().reset_index()
    sentiment_daily["next_day"] = pd.to_datetime(sentiment_daily["date_only"]) + pd.Timedelta(days=1)
    
    merged = pd.merge(sentiment_daily, stock_df, left_on="next_day", right_on="date_only", how="inner")

    if len(merged) >= 2:
        corr, pval = pearsonr(merged["compound"], merged["stock_close"])
        print(f"[{stock_symbol}] Correlation between sentiment and next-day close: {corr:.4f} (p={pval:.4f})")
        sns.regplot(x="compound", y="stock_close", data=merged)
        plt.title(f"Sentiment vs. Next-Day Stock Price for {stock_symbol}")
        plt.xlabel("Avg. Sentiment (Compound)")
        plt.ylabel("Next-Day Stock Price")
        plt.grid(True)
        plt.show()
    else:
        corr, pval = None, None
        print(f"[{stock_symbol}] Not enough data to compute correlation.")
    return merged, corr, pval
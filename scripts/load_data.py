import os
import pandas as pd

def load_news_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["date"])
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    df["date_only"] = df["date"].dt.date
    return df

def load_stock_data(ticker, stock_data_dir="../data"):
    stock_path = os.path.join(stock_data_dir, f"{ticker}_historical_data.csv")
    stock_df = pd.read_csv(stock_path)

    # Standardize column names to lowercase and replace spaces with underscores
    stock_df.columns = [col.lower().strip().replace(" ", "_") for col in stock_df.columns]

    # Parse date column
    if "date" in stock_df.columns:
        stock_df["date"] = pd.to_datetime(stock_df["date"])
    else:
        raise ValueError(f"'date' column not found in {ticker} data.")

    # Ensure all required columns exist
    required_cols = ["date", "open", "high", "low", "close", "volume"]
    missing_cols = [col for col in required_cols if col not in stock_df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in {ticker} data: {missing_cols}")

    # Subset, sort, and drop missing rows
    stock_df = stock_df[required_cols].sort_values("date").dropna()

    return stock_df

import pandas as pd

def load_news_data(filepath):
    df = pd.read_csv(filepath, parse_dates=["date"])
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    df["date_only"] = df["date"].dt.date
    return df
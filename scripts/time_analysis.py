import pandas as pd

def add_date_columns(df):
    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date_only'] = df['date'].dt.date
    df['hour'] = df['date'].dt.hour
    return df

def get_articles_per_day(df):
    return df['date_only'].value_counts().sort_index()

def get_articles_by_hour(df):
    return df['hour'].value_counts().sort_index()

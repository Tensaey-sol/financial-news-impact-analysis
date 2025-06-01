import matplotlib.pyplot as plt
import seaborn as sns

def describe_headlines(news_df):
    news_df["headline_len"] = news_df["headline"].apply(len)
    print(news_df["headline_len"].describe())

def analyze_publishers(news_df):
    publisher_counts = news_df["publisher"].value_counts()
    print("\nTop Publishers:\n", publisher_counts.head())

def plot_articles_per_day(news_df):
    articles_per_day = news_df.groupby("date_only").size()
    articles_per_day.plot(figsize=(12, 4), title="Articles Per Day")
    plt.ylabel("Count")
    plt.show()

def plot_publishing_hour(news_df):
    news_df["hour"] = news_df["date"].dt.hour
    sns.histplot(news_df["hour"], bins=24)
    plt.title("Publishing Time of Day")
    plt.xlabel("Hour")
    plt.show()
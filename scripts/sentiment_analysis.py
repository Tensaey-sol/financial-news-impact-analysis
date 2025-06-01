import seaborn as sns
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def compute_sentiment(news_df):
    analyzer = SentimentIntensityAnalyzer()
    news_df["compound"] = news_df["headline"].apply(lambda x: analyzer.polarity_scores(x)["compound"])
    news_df["sentiment"] = news_df["compound"].apply(
        lambda x: "positive" if x > 0.05 else "negative" if x < -0.05 else "neutral"
    )

def plot_sentiment_distribution(news_df):
    sns.countplot(data=news_df, x="sentiment")
    plt.title("Sentiment Distribution")
    plt.show()
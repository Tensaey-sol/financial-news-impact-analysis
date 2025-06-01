import re
import nltk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud


nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    return " ".join([word for word in tokens if word not in stop_words])

def apply_cleaning(news_df):
    news_df["clean_headline"] = news_df["headline"].apply(clean_text)

def plot_wordcloud(news_df):
    text = " ".join(news_df["clean_headline"].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Headline Keyword WordCloud")
    plt.show()

def plot_top_keywords(text_series, n=20):
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(text_series.dropna())
    freqs = X.sum(axis=0).A1
    terms = vectorizer.get_feature_names_out()
    freq_df = pd.DataFrame({'term': terms, 'freq': freqs})
    freq_df = freq_df.sort_values(by='freq', ascending=False).head(n)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=freq_df, x='freq', y='term')
    plt.title("Top Keywords in Headlines")
    plt.xlabel("Frequency")
    plt.ylabel("Keyword")
    plt.tight_layout()
    plt.show()

def plot_tfidf_top_terms(text_series, n_terms=20):
    vectorizer = TfidfVectorizer(max_features=n_terms, stop_words='english')
    X = vectorizer.fit_transform(text_series.dropna())
    features = vectorizer.get_feature_names_out()
    scores = X.sum(axis=0).A1

    tfidf_df = pd.DataFrame({'term': features, 'score': scores})
    tfidf_df = tfidf_df.sort_values(by='score', ascending=False)

    tfidf_df.plot.barh(x='term', y='score', figsize=(10, 6), legend=False)
    plt.title("Top TF-IDF Terms")
    plt.xlabel("Score")
    plt.tight_layout()
    plt.show()

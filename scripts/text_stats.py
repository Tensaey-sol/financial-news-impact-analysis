from sklearn.feature_extraction.text import CountVectorizer

def add_headline_length(df):
    df['headline_length'] = df['headline'].apply(len)
    return df

def get_headline_length_stats(df):
    return df['headline_length'].describe()

def extract_top_keywords(df, max_features=50):
    vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english', max_features=max_features)
    X = vectorizer.fit_transform(df['headline'])
    return vectorizer.get_feature_names_out()

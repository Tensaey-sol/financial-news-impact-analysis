def count_articles_per_publisher(df):
    return df['publisher'].value_counts()

def extract_publisher_domains(df):
    df['publisher_domain'] = df['publisher'].apply(lambda x: x.split('@')[1] if '@' in x else 'N/A')
    return df['publisher_domain'].value_counts()
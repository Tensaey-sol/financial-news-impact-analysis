import seaborn as sns
import matplotlib.pyplot as plt

def extract_domain(publisher):
    if "@" in publisher:
        return publisher.split("@")[1].lower()
    return publisher.lower()

def analyze_domains(news_df):
    news_df["publisher_domain"] = news_df["publisher"].apply(extract_domain)
    domain_counts = news_df["publisher_domain"].value_counts().head(10)
    print("\nTop Email Domains:\n", domain_counts)

    sns.barplot(x=domain_counts.values, y=domain_counts.index)
    plt.title("Top Publishing Domains")
    plt.xlabel("Article Count")
    plt.show()

# TASK-02 SENTIMENT ANALYSIS PROJECT
# TOPIC: Apple vs Samsung - Public Opinion Analysis


import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

# ---------------------------------------------------------
# 1. CREATE SAMPLE SOCIAL MEDIA DATASET
# ---------------------------------------------------------

data = {
    "tweet": [
        "I love the new Apple iPhone, camera quality is best!",
        "Samsung battery life is amazing.",
        "Apple phones are too expensive.",
        "Samsung UI is bad and full of lag.",
        "I am happy with my Apple device!",
        "Samsung gives best performance for the price.",
        "Apple ecosystem is awesome and smooth.",
        "I hate Samsung phones, bad software.",
        "Apple customer service is terrible.",
        "Samsung display quality is fantastic!",
        "Apple processor is fastest.",
        "Samsung phones overheat sometimes.",
        "I liked the new Apple launch event.",
        "Samsung camera performs extremely well.",
        "Apple battery drains so fast!",
    ],
    "brand": [
        "Apple", "Samsung", "Apple", "Samsung", "Apple",
        "Samsung", "Apple", "Samsung", "Apple", "Samsung",
        "Apple", "Samsung", "Apple", "Samsung", "Apple"
    ]
}

df = pd.DataFrame(data)

print("Dataset Loaded:\n")
print(df.head())

# ---------------------------------------------------------
# 2. TEXT PREPROCESSING
# ---------------------------------------------------------

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["clean"] = df["tweet"].apply(clean_text)

# ---------------------------------------------------------
# 3. SENTIMENT LEXICON
# ---------------------------------------------------------

positive = set(["good","great","awesome","amazing","fantastic","love","best","happy","smooth","liked","fast","excellent"])
negative = set(["bad","terrible","hate","worst","expensive","lag","drains","overheat"])

def analyze_sentiment(text):
    tokens = text.split()
    pos = sum(1 for t in tokens if t in positive)
    neg = sum(1 for t in tokens if t in negative)
    score = pos - neg

    if score > 0:
        label = "positive"
    elif score < 0:
        label = "negative"
    else:
        label = "neutral"

    return pd.Series([pos, neg, score, label])

df[["pos","neg","score","sentiment"]] = df["clean"].apply(analyze_sentiment)

print("\nSentiment Analysis Completed:\n")
print(df)

# ---------------------------------------------------------
# 4. VISUALIZATIONS
# ---------------------------------------------------------

# Histogram of Sentiment Score
plt.figure(figsize=(7,5))
plt.hist(df["score"], bins=5)
plt.title("Sentiment Score Distribution")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Brand-wise Sentiment Count
plt.figure(figsize=(7,5))
sns.countplot(x=df["brand"], hue=df["sentiment"])
plt.title("Apple vs Samsung - Sentiment Comparison")
plt.show()

# Pie Chart for Overall Sentiments
plt.figure(figsize=(6,6))
df["sentiment"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Overall Sentiment Distribution")
plt.ylabel("")
plt.show()

# ---------------------------------------------------------
# 5. WORDCLOUDS
# ---------------------------------------------------------

# Apple WordCloud
apple_text = " ".join(df[df["brand"]=="Apple"]["clean"])
apple_wc = WordCloud(width=800, height=400, background_color='white').generate(apple_text)

plt.figure(figsize=(10,5))
plt.imshow(apple_wc)
plt.axis("off")
plt.title("Apple WordCloud")
plt.show()

# Samsung WordCloud
samsung_text = " ".join(df[df["brand"]=="Samsung"]["clean"])
samsung_wc = WordCloud(width=800, height=400, background_color='white').generate(samsung_text)

plt.figure(figsize=(10,5))
plt.imshow(samsung_wc)
plt.axis("off")
plt.title("Samsung WordCloud")
plt.show()

# ---------------------------------------------------------
# 6. FINAL SUMMARY
# ---------------------------------------------------------

print("\nFinal Sentiment Summary:\n")
print(df.groupby("brand")["sentiment"].value_counts())
print("\nInsights:")
print("- Apple: more positive than negative tweets in this sample, but complaints about price/battery.")
print("- Samsung: praise for battery, camera, display; some negatives about UI and heating.")

print("\nProject Completed Successfully!")

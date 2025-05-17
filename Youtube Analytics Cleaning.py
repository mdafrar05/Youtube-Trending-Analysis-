import pandas as pd

# Load the dataset
df = pd.read_csv("Trending Video Dataset.csv")

# Drop unnecessary columns
df.drop(columns=["index", "video_error_or_removed"], inplace=True, errors='ignore')

# Convert trending_date to datetime (format: yy.dd.mm)
df["trending_date"] = pd.to_datetime(df["trending_date"], format="%y.%d.%m", errors='coerce')

# Convert publish_date to date only
df["publish_date"] = pd.to_datetime(df["publish_date"], errors='coerce' , dayfirst=True).dt.date

# Replace '[none]' in tags and fill NA with empty string
df["tags"] = df["tags"].replace("[none]", "").fillna("")

# Drop rows with missing critical fields (title, views)
df.dropna(subset=["title", "views"], inplace=True)

# Convert key numeric columns to numeric dtype
numeric_cols = ["views", "likes", "dislikes", "comment_count"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

# Create trending_days count per video_id
trending_days = df.groupby("video_id")["trending_date"].nunique().reset_index()
trending_days.columns = ["video_id", "trending_days"]
df = df.merge(trending_days, on="video_id", how="left")

import pandas as pd

# Load your dataset (replace with your path if needed)
df = pd.read_csv("Trending Video Dataset.csv", encoding='utf-8')

# Define simple keyword-based sentiment rules
positive_keywords = ['funny', 'awesome', 'inspiring', 'great', 'love', 'amazing', 'happy', 'cool']
negative_keywords = ['fail', 'worst', 'angry', 'hate', 'bad', 'disgusting', 'sad', 'cry']

def get_sentiment(tag_text):
    if pd.isna(tag_text):
        return 'Neutral'
    
    tag_text = tag_text.lower()
    if any(word in tag_text for word in positive_keywords):
        return 'Positive'
    elif any(word in tag_text for word in negative_keywords):
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment function to the tags column
df['Sentiment'] = df['tags'].apply(get_sentiment)

# Save to a new CSV file
df.to_csv("Trending_Video_Sentiment_Output.csv", index=False)

print("Sentiment analysis completed. File saved as 'Trending_Video_Sentiment_Output.csv'.")


# Export cleaned CSV
df.to_csv("Youtube_trending_analysis.csv", index=False)

print("✅ Cleaned CSV saved as 'Cleaned_YT_Trending.csv'")

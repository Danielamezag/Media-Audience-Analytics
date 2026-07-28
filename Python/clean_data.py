import pandas as pd

df = pd.read_csv("media_audience_analytics_youtube_data.csv")

df['published_at'] = pd.to_datetime(df.published_at)

df['tags'] = df['tags'].fillna('No Tags')

df['engagement_rate'] = (df['likes'] + df['comments']) / df['views']
df.info()

print(df.duplicated().sum())
print(df.isnull().sum())

df.to_csv('cleaned_media_data.csv', index = False)
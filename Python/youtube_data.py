pip install google-api-python-client pandas

from googleapiclient.discovery import build
import pandas as pd

API_KEY = "AIzaSyAJ3eDEntjtcwOhm_wuvMaZ2baI0sV7TIA"

youtube = build("youtube", "v3", developerKey=API_KEY)

channel_ids = {
    "FOX News": "UCXIJgqnII2ZOINSWNOGFThA",
    "NBC News": "UCeY0bbntWzzVIaj2z3QigXg",
    "ABC News": "UCBi2mrWuNuyYy4gbM6fU18Q",
    "CBS News": "UC8p1vwvWtl6T73JiExfWs1g"
}

def get_uploads_playlist(channel_id):
    request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )
    response = request.execute()
    return response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

def get_video_ids(playlist_id, max_videos=300):
    video_ids = []
    next_page_token = None

    while len(video_ids) < max_videos:
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response["items"]:
            video_ids.append(item["contentDetails"]["videoId"])

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return video_ids[:max_videos]

def get_video_details(video_ids, channel_name):
    all_video_data = []

    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]

        request = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=",".join(batch)
        )
        response = request.execute()

        for video in response["items"]:
            snippet = video["snippet"]
            stats = video.get("statistics", {})

            all_video_data.append({
                "channel": channel_name,
                "video_id": video["id"],
                "title": snippet.get("title"),
                "published_at": snippet.get("publishedAt"),
                "description": snippet.get("description"),
                "tags": ", ".join(snippet.get("tags", [])),
                "category_id": snippet.get("categoryId"),
                "views": stats.get("viewCount", 0),
                "likes": stats.get("likeCount", 0),
                "comments": stats.get("commentCount", 0)
            })

    return all_video_data

all_data = []

for channel_name, channel_id in channel_ids.items():
    print(f"Collecting data for {channel_name}...")

    uploads_playlist = get_uploads_playlist(channel_id)
    video_ids = get_video_ids(uploads_playlist, max_videos=300)
    video_data = get_video_details(video_ids, channel_name)

    all_data.extend(video_data)

df = pd.DataFrame(all_data)

df["views"] = pd.to_numeric(df["views"])
df["likes"] = pd.to_numeric(df["likes"])
df["comments"] = pd.to_numeric(df["comments"])

df.head()

df.to_csv("media_audience_analytics_youtube_data.csv", index=False)
from googleapiclient.discovery import build

# Replace with your API key
API_KEY = "AIzaSyA1Rw6N4N_rXnsuK4L5_iIvVWZLgvNO3yc"

# Replace with the channel's username or channel ID
CHANNEL_ID = "UCcYzLCs3zrQIBVHYA1sK2sw"

# Create a YouTube Data API service instance
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_video_urls(channel_id):
    video_urls = []

    # Get the uploads playlist ID of the channel
    response = youtube.channels().list(part="contentDetails", id=channel_id).execute()
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Retrieve all video IDs from the uploads playlist
    next_page_token = None
    while True:
        playlist_items_response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        video_ids = [item["contentDetails"]["videoId"] for item in playlist_items_response["items"]]
        video_urls.extend(["https://www.youtube.com/watch?v=" + video_id for video_id in video_ids])

        next_page_token = playlist_items_response.get("nextPageToken")
        if not next_page_token:
            break

    return video_urls

if __name__ == "__main__":
    video_urls = get_channel_video_urls(CHANNEL_ID)
    for url in video_urls:
        print(url)

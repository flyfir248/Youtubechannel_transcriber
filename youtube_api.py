import yt_dlp

channel_url = "https://www.youtube.com/@sadhguru/videos"

ydl_opts = {
    'extract_flat': True,  # Extract all URLs, not just video URLs
    'quiet': True,         # Suppress output
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    result = ydl.extract_info(channel_url, download=False)
    if 'entries' in result:
        for entry in result['entries']:
            if entry.get('url'):
                print(entry['url'])

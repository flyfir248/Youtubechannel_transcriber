from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import wordninja


def fix_clubbed_text(text):
    # Use regex to split words that are concatenated without spaces
    fixed_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return fixed_text


def split_clubbed_words(text):
    split_words = []
    for word in text.split():
        split_words.extend(wordninja.split(word))
    return ' '.join(split_words)


# Read video URLs from the file
with open("Sadguruyoutubevideourls.txt", "r") as file:
    video_urls = file.readlines()

# Process each video URL
for vid_url in video_urls:
    vid_url = vid_url.strip()  # Remove leading/trailing whitespace
    vid_id = vid_url.split("v=")[-1]

    try:
        data = yta.get_transcript(vid_id)
        transcript = ''

        for value in data:
            for key, val in value.items():
                if key == 'text':
                    transcript += val

        # Clean and fix clubbed text
        transcript = fix_clubbed_text(transcript)

        # Split clubbed words using wordninja
        transcript = split_clubbed_words(transcript)

        with open("Transcripts.txt", 'a') as file:
            file.write(transcript + '\n')

        print(f"Transcript saved for video: {vid_url}")

    except Exception as e:
        print(f"Error processing video {vid_url}: {e}")

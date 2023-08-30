# Python Scripts Documentation

This repository contains four Python scripts that perform various tasks using different libraries and APIs. Each script has a specific purpose and usage. Below, you'll find a brief overview of each script along with instructions on how to use them.
### 1. PDF Generation Script

File: pdf_generation_script.py

This script uses the reportlab library to convert a plain text file into a PDF document. It takes an input text file, processes its content, and generates a PDF with formatted paragraphs and spacing.
Usage:

    Modify the input_filename and output_filename variables in the script to specify the input text file's name and the desired output PDF file's name.
    Run the script using a Python interpreter.
    The generated PDF will be saved in the same directory with the provided output filename.

### 2. YouTube Channel Video URLs Script

File: youtube_channel_video_urls.py

This script utilizes the YouTube Data API to fetch the video URLs from a specific YouTube channel. You need to provide your own API key and the channel's username or ID.
Usage:

    Replace the API_KEY and CHANNEL_ID variables with your own API key and the target channel's username or ID.
    Run the script using a Python interpreter.
    The script will fetch and display the URLs of videos uploaded to the specified channel.

### 3. YouTube Video Transcripts Script

File: youtube_video_transcripts.py

This script uses the youtube_transcript_api library to fetch and process video transcripts from a list of YouTube video URLs. The cleaned and split text is then saved to a file.
Usage:

    Create a text file named Sadguruyoutubevideourls.txt and list the YouTube video URLs (one URL per line).
    Run the script using a Python interpreter.
    The script will process each video URL, fetch its transcript, clean and split the text, and save it to the Transcripts.txt file.

### 4. YouTube Channel URL Extraction Script

File: youtube_channel_url_extraction.py

This script utilizes the yt_dlp library to extract URLs from a YouTube channel's page. It extracts all URLs, not just video URLs.
Usage:

    Modify the channel_url variable with the URL of the target YouTube channel.
    Run the script using a Python interpreter.
    The script will extract and display all URLs from the specified YouTube channel's page.

### Demonstration:

The youtube_video_transcripts.py script has been successfully used to collect transcripts for over 2000 videos from the Sadguru YouTube channel. The script processed each video URL, fetched its transcript, cleaned and split the text, and stored it in the Transcripts.txt file. The collected transcripts can be found in the Transcripts.txt file in this repository.
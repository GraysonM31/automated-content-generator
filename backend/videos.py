# Imports
import requests
import os
from dotenv import load_dotenv

# Variables
# Load environment variables from .env file
load_dotenv('.venv')

# Access the API_KEY variable
key = os.getenv('P_API_KEY', "ovLulnSguzJN0lFRIXa3ktFfV5HCQ6NkIkQiCrVB4IgGNBzK1zaJ2gUv")

def downloadVideo(url, filename):

    # Send the Request
    response = requests.get(url, stream=True)

    # Download the Video
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

# Get Stock Videos from Pexels API
def getStockVideos(query, num):

    # Set Headers and Build URL
    headers = {'Authorization': key}
    url = f"https://api.pexels.com/videos/search?query={query}&per_page={num}"

    # Send the Request
    r = requests.get(url, headers=headers)

    # Parse the Response
    response = r.json()

    # Variables
    urls = []
    videos = []

    # Itterate Through Videos
    for i in range(0, num):

        # Get Video URL's
        urls = response["videos"][i]["video_files"]
        temp_video_url = ""
        
        # Create the temp directory if it doesn't exist
        if not os.path.exists("temp"):
            os.makedirs("temp")

        # TESTING !!!!!!!!!!!!!!
        if os.path.exists("temp"):
            files = os.listdir("temp")
            if files:
                for file in files:
                    os.remove(os.path.join("temp", file))



        # Itterate Through Videos
        for video in urls:

            # Check for Downloadable Videos
            if ".com/video-files" in video["link"]:
                temp_video_url = video["link"]
                    
        # Append Video URL
        if temp_video_url != "":
            videos.append(temp_video_url)

    # Download Videos
    for i in range(0, len(videos)):
        downloadVideo(videos[i], f"temp/{i + 1}.mp4")

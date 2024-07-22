from moviepy.editor import VideoFileClip
import os

# Get the path to the "temp" folder
folder_path = "/temp"

# Get a list of all the video files in the folder
video_files = [file for file in os.listdir(folder_path) if file.endswith(".mp4") or file.endswith(".mp3")]

# Process each video clip
for file in video_files:
    input_path = os.path.join(folder_path, file)
    output_path = os.path.join(folder_path, f"resized_{file}")

    # Load the clip
    clip = VideoFileClip(input_path)

    # Resize the clip to 1280x720
    resized_clip = clip.resize(1280, 720)

    # Save the resized clip to a new file
    resized_clip.write_videofile(output_path)


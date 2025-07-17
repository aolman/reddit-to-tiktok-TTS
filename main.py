from reddit.fetch_posts import fetch_posts
from tts.generate_audio import text_to_speech
from video.create_video import merge_audio_with_video, merge_captions_with_video
import json

post = fetch_posts()

with open("config/settings.json") as f:
    config = json.load(f)
combined_text = f"{post['title']}\n\n{post['body']}"
audio_path = "output/narration.mp3"
text_to_speech(combined_text, audio_path)
video_path = "video/assets/background.mp4"
output_path = "output/final_video.mp4"
video = merge_audio_with_video(audio_path, video_path)
merge_captions_with_video(combined_text, video, output_path)
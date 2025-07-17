from moviepy import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip

def merge_audio_with_video(audio_path, video_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video.audio = audio
    video = video.subclipped(0, audio.duration)
    return video
    
def merge_captions_with_video(text, video, output_path):
    txt_clip = TextClip(text=text, font_size=40, color='white',
                   stroke_color='black', text_align='center', duration=video.duration)
    video_with_text = CompositeVideoClip([video, txt_clip])
    video_with_text.write_videofile(output_path, codec='libx264', audio_codec='aac')
    
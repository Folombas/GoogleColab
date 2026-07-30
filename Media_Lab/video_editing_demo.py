import os
from moviepy.config import change_settings
from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert"})

clip = ColorClip(size=(1280, 720), color=[50, 50, 200], duration=5)
txt_clip = TextClip("Python + Video Editing", fontsize=70, color='white')
txt_clip = txt_clip.set_position('center').set_duration(5)
video = CompositeVideoClip([clip, txt_clip])
video.write_videofile("result.mp4", fps=24)
from moviepy import *

from mp3_maker import mp3_files

for i in range(0, len(mp3_files)-1):
    video = VideoFileClip("myHolidays.mp4").subclip(i*60,(i+1)*60)
    audio = AudioFileClip(mp3_files[i])
    video.set_audio(audio)

    # TODO: add the subtitle thing

    filename = 'p' + i + '.mp4'
    video.write_videofile(filename)

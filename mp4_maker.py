from moviepy import *

from mp3_maker import mp3_files

for i in range(0, len(mp3_files)):
    video = VideoFileClip("myHolidays.mp4").subclip(i*60,(i+1)*60)

    # TODO: add the subtitle thing

    result = CompositeVideoClip([video])
    filename = 'p' + i + '.mp4'
    result.write_videofile(filename, fps=25)

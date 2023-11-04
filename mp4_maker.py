from moviepy.editor import *

from mp3_maker import mp3_files

count = 0
index = 0
while index < len(mp3_files):
    audios = []
    duration = 0
    for i in range(index, len(mp3_files)):
        curr = AudioFileClip(mp3_files[i])
        if duration + curr.duration > 60:
            break
        duration += curr.duration
        audios.append(curr)
        index += 1

    audio = concatenate_audioclips(audios)
    video = VideoFileClip("minecraft.mp4").subclip(count*60,(count+1)*60).subclip(0, audio.duration)
    video.audio = concatenate_audioclips(audios)

    # TODO: add the subtitle thing

    filename = 'p' + str(count) + '.mp4'
    cropped = video.fx(vfx.crop, x1=video.w//3, x2=(video.w//3)*2)
    cropped.write_videofile(filename)
    count += 1

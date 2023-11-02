from moviepy.editor import *

from mp3_maker import mp3_files

count = 0
index = 0
while index < len(mp3_files):
    video = VideoFileClip("minecraft.mp4").subclip(count*60,(count+1)*60)
    audios = []
    duration = 0
    for i in range(index, len(mp3_files)):
        curr = AudioFileClip(mp3_files[i])
        if duration + curr.duration > 60:
            break
        duration += curr.duration
        audios.append(curr)
        index += 1

    concat_audio = concatenate_audioclips(audios)
    video.set_audio(concat_audio)

    # TODO: add the subtitle thing

    filename = 'p' + count + '.mp4'
    video.write_videofile(filename)
    count += 1

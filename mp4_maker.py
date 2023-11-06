from moviepy.editor import *
import os

def export(cwd, file):
    mp3_files = [file]

    timeLimit = 60
    count = 0
    index = 0
    
    # go through the list and generate the videos until u run out of mp3 files
    while index < len(mp3_files):
        # list of AudioFlieCips from mp3_files
        audios = []

        # add the audio to the list until right before it exceeds the timeLimit
        duration = 0
        for i in range(index, len(mp3_files)):
            curr = AudioFileClip(cwd + mp3_files[i])
            if duration + curr.duration > timeLimit:
                break
            duration += curr.duration
            audios.append(curr)
            index += 1

        # concatenate the list of audios into one CompositeAudioClip
        audio = concatenate_audioclips(audios)

        # take a subclip of the video, to the duration of the audio clip
        video = VideoFileClip("minecraft.mp4").subclip(count*timeLimit,(count+1)*timeLimit).subclip(0, audio.duration)

        # set the concatenated audio as the video audio
        video.audio = audio

        # crop video to fit the YouTube Short w/h ratio
        cropped = video.fx(vfx.crop, x1=video.w//3, x2=(video.w//3)*2)

        # write to file
        filename = 'p' + str(count) + '.mp4'
        cropped.write_videofile(filename)
        count += 1

    for i in range(0, count):
        #===============================================================
        # type the subtitle command for each mp4 file that was generated
        #===============================================================
        filename = 'p' + str(count) + '.mp4'
        os.system("auto_subtitle " + filename + " -o subtitled/")
        break

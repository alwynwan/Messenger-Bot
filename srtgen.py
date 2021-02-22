from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.video.fx as vfx

def create_srt(line):
    subs_obj = open(r"D:\Final Renders\your next line.srt", "r")
    orig_subs = subs_obj.read().split("\n")

    print(orig_subs)

    orig_subs[6] = f"\"{line}\""
    orig_subs[10] = line

    new_srt = open(r"D:\Final Renders\result.srt", "w")

    for x in orig_subs:
        new_srt.write(x + "\n")

    new_srt.close()
    subs_obj.close()

def composite_gif(line):
    video = VideoFileClip(r"D:\Final Renders\tsuginiomaewa.mp4")
    video = vfx.resize.resize(video,0.5)
    generator = lambda txt: TextClip(txt, font='Arial',fontsize=16, color='white')

    create_srt(line)
    sub = SubtitlesClip(r"D:\Final Renders\result.srt", generator)

    result = CompositeVideoClip([video, sub.set_position(('center','bottom'))])
    result.write_gif(r"D:\Final Renders\result.gif",fps=10,program="ffmpeg", fuzz=100,colors=2)
    result.close()
    video.close()
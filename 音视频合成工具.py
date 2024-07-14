#coding=GBK
"""
为我用python编写一个程序实现以下功能：
将一个视频文件和一个音频文件合并为一个同时具有音频和视频的文件

程序输入输出有以下规定：
命令行输入"-v VideoPath -a AudioPath [-o OutPath] | -?"
VideoPath是一个音频文件，格式为.m4a、.mp3或者.aac
AudioPath是一个视频文件的路径，格式为.mp4或者.avi
OutPath是输出文件的路径，当该项未被给出时默认为"./output.mp4"
该程序将VideoPath和AudioPath两个文件合并为一个同时具有音频和视频的文件，文件的格式由OutPath指定
当参数中给出"-?"时不执行上述功能而是输出使用说明，即介绍各参数的用法

程序满足以下要求：
使用moviepy库
程序中应有适当的容错处理，
若"-v"和"-a"参数不全或路径错误应当进行提示并不进行继续操作
"""

# 以下代码段由OpenAI的ChatGPT助手编写

import argparse
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def merge_video_audio(video_path, audio_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        video_with_audio = video_clip.set_audio(audio_clip)
        video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')
        print(f"合并成功，输出文件保存在: {output_path}")

    except Exception as e:
        print(f"合并过程中出现错误: {str(e)}")

def print_usage():
    def __back(list:list):
        return list[list.__len__()-1]
    print("使用说明:")
    print("%s -v VideoPath -a AudioPath [-o OutPath] | -?"%(__back(__file__.split('\\'))))
    print("-v VideoPath   : 视频文件路径 (格式: .mp4 或 .avi)")
    print("-a AudioPath   : 音频文件路径 (格式: .m4a, .mp3 或 .aac)")
    print("-o OutPath     : 输出文件路径，默认为 '.\\output.mp4'")
    print("-?             : 显示使用说明")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="合并视频和音频文件")
    parser.add_argument("-v", dest="video_path", help="视频文件路径")
    parser.add_argument("-a", dest="audio_path", help="音频文件路径")
    parser.add_argument("-o", dest="output_path", default="./output.mp4", help="输出文件路径，默认为 './output.mp4'")
    parser.add_argument("-?", dest="show_usage", action="store_true", help="显示使用说明")

    args = parser.parse_args()

    if args.show_usage:
        print_usage()
    elif args.video_path and args.audio_path:
        if os.path.exists(args.video_path) and os.path.exists(args.audio_path):
            merge_video_audio(args.video_path, args.audio_path, args.output_path)
        else:
            print("错误: 视频文件或音频文件路径不存在")
            print_usage()
    else:
        print("错误: 请提供正确的视频文件和音频文件路径")
        print_usage()

# 以上代码段由OpenAI的ChatGPT助手编写
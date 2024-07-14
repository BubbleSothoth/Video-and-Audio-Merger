#coding=GBK
"""
Ϊ����python��дһ������ʵ�����¹��ܣ�
��һ����Ƶ�ļ���һ����Ƶ�ļ��ϲ�Ϊһ��ͬʱ������Ƶ����Ƶ���ļ�

����������������¹涨��
����������"-v VideoPath -a AudioPath [-o OutPath] | -?"
VideoPath��һ����Ƶ�ļ�����ʽΪ.m4a��.mp3����.aac
AudioPath��һ����Ƶ�ļ���·������ʽΪ.mp4����.avi
OutPath������ļ���·����������δ������ʱĬ��Ϊ"./output.mp4"
�ó���VideoPath��AudioPath�����ļ��ϲ�Ϊһ��ͬʱ������Ƶ����Ƶ���ļ����ļ��ĸ�ʽ��OutPathָ��
�������и���"-?"ʱ��ִ���������ܶ������ʹ��˵���������ܸ��������÷�

������������Ҫ��
ʹ��moviepy��
������Ӧ���ʵ����ݴ���
��"-v"��"-a"������ȫ��·������Ӧ��������ʾ�������м�������
"""

# ���´������OpenAI��ChatGPT���ֱ�д

import argparse
from moviepy.editor import VideoFileClip, AudioFileClip
import os

def merge_video_audio(video_path, audio_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        video_with_audio = video_clip.set_audio(audio_clip)
        video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')
        print(f"�ϲ��ɹ�������ļ�������: {output_path}")

    except Exception as e:
        print(f"�ϲ������г��ִ���: {str(e)}")

def print_usage():
    def __back(list:list):
        return list[list.__len__()-1]
    print("ʹ��˵��:")
    print("%s -v VideoPath -a AudioPath [-o OutPath] | -?"%(__back(__file__.split('\\'))))
    print("-v VideoPath   : ��Ƶ�ļ�·�� (��ʽ: .mp4 �� .avi)")
    print("-a AudioPath   : ��Ƶ�ļ�·�� (��ʽ: .m4a, .mp3 �� .aac)")
    print("-o OutPath     : ����ļ�·����Ĭ��Ϊ '.\\output.mp4'")
    print("-?             : ��ʾʹ��˵��")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="�ϲ���Ƶ����Ƶ�ļ�")
    parser.add_argument("-v", dest="video_path", help="��Ƶ�ļ�·��")
    parser.add_argument("-a", dest="audio_path", help="��Ƶ�ļ�·��")
    parser.add_argument("-o", dest="output_path", default="./output.mp4", help="����ļ�·����Ĭ��Ϊ './output.mp4'")
    parser.add_argument("-?", dest="show_usage", action="store_true", help="��ʾʹ��˵��")

    args = parser.parse_args()

    if args.show_usage:
        print_usage()
    elif args.video_path and args.audio_path:
        if os.path.exists(args.video_path) and os.path.exists(args.audio_path):
            merge_video_audio(args.video_path, args.audio_path, args.output_path)
        else:
            print("����: ��Ƶ�ļ�����Ƶ�ļ�·��������")
            print_usage()
    else:
        print("����: ���ṩ��ȷ����Ƶ�ļ�����Ƶ�ļ�·��")
        print_usage()

# ���ϴ������OpenAI��ChatGPT���ֱ�д
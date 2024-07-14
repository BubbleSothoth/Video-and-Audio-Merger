# Video-and-Audio-Merger
将一个视频文件和一个音频文件合并为一个同时具有音频和视频的文件的小工具，仅支持命令行使用
# 使用方法
命令行输入"-v VideoPath -a AudioPath [-o OutPath] | -?"
VideoPath是一个音频文件，格式为.m4a、.mp3或者.aac等
AudioPath是一个视频文件的路径，格式为.mp4或者.avi
OutPath是输出文件的路径，当该项未被给出时默认为"./output.mp4"
该程序将VideoPath和AudioPath两个文件合并为一个同时具有音频和视频的文件，文件的格式由OutPath指定
当参数中给出"-?"时不执行上述功能而是输出使用说明，即介绍各参数的用法

# 运行环境
## OS
Windows10及以上
## 解释器
Python 3.10.5
## 备注
确定你的python支持moviepy库

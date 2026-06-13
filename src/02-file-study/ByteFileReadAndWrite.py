"""
二进制文件读写
"""
import os.path

# 获取当前脚本所在目录
dir_path = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(dir_path, "data", "c.txt")

# 用二进制方式写出文本
with open(filePath, "wb") as f:
    f.write(b"hello file")


dir_path = os.path.dirname(os.path.abspath(__file__))
filePathOrigin = os.path.join(dir_path, "data", "0cd69033-43ed-495a-a2ee-747061af366bIP64.jpg")
filePathCurrent = os.path.join(dir_path, "data", "hyq.jpg")

# 用二进制方式复制图片
with open(filePathOrigin, "rb") as f:
    byte = f.read()
with open(filePathCurrent, "wb") as f:
    f.write(byte)



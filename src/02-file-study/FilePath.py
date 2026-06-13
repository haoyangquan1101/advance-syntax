"""
文件读取
"""
import os.path

# 获取当前脚本所在目录
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

filePath = os.path.join(dir_path, "data", "a.txt")
print(filePath)

print(os.path.isfile(filePath))
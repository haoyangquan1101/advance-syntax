"""
文本文件读写
"""
import os.path

# 获取当前脚本所在目录
dir_path = os.path.dirname(os.path.abspath(__file__))

filePath = os.path.join(dir_path, "data", "b.txt")

with open(filePath, "w", encoding="utf-8") as f:
    f.write("hello file\n")
    f.write("hello file\n")
    f.write("hello file\n")
    f.write("hello file\n")

# a 模式是追加 不会清空原来的内容
# os.linesep 换行符
with open(filePath, "w", encoding="utf-8") as f:
    lines = ["hello file"+os.linesep, "hello file"+os.linesep, "hello file"+os.linesep, "hello file"+os.linesep]
    f.writelines(lines)

# print输出到文件
with open(filePath, "w", encoding="utf-8") as f:
    lines = ["hello file"+os.linesep, "hello file"+os.linesep, "hello file"+os.linesep, "hello file"+os.linesep]
    for line in lines:
        print(line,file=f)
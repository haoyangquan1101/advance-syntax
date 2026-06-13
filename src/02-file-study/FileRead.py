"""
文件读取
open(文件名,模式)
"""
filePath = "data/a.txt"
file = open(filePath, "r", encoding="utf-8")
content = file.read()
print(content)
file.close()




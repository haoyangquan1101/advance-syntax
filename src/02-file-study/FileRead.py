"""
文件读取
open(文件名,模式)
"""
filePath = "data/a.txt"
file = open(filePath, "r", encoding="utf-8")

# read 读取全部
content = file.read()
print(content)

# readline 读取行 size指定读取行数 适用于大型文本文档
with open(filePath, "r", encoding="utf-8") as file2:
    content2 = file2.readline(10)

# readlines 读取所有行 返回列表
with open(filePath, "r", encoding="utf-8") as file3:
    content3 = file3.readlines()
    print(f"contet3{content3}")

    for index,line in enumerate(content3):
        print(f"index:{index},line:{line}")

file.close()




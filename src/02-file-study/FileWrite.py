"""
文件写入
"""

# file操作的标准格式
filePath = "data/a.txt"
file = open(filePath, "w", encoding="utf-8")
"""
# 读或写
file.write("Hello, World!")

# 关闭资源
file.close()
print("-"*30)
"""

# 以上代码并不能保证file.close()一定执行
# try finally
try:
    file = open(filePath, "w", encoding="utf-8")
    file.write("Hello, World!")
finally:
    if file:
        file.close()

# with
with open(filePath, "w", encoding="utf-8") as file:
    file.write("Hello, World!")

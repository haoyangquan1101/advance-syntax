"""
函数的嵌套调用
"""

def function_A():
    print("\t函数 A 开始执行")
    print("\t函数 A 执行中...")
    print("\t函数 A 结束执行")

def function_B():
    print("函数 B 开始执行")
    print("函数 B 执行中...")
    function_A()  # 嵌套调用函数 A
    print("函数 B 执行中...")
    print("函数 B 结束执行")

# 调用外层函数
function_B()
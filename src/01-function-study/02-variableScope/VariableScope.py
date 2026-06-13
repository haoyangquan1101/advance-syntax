"""
变量作用域
"""

# 局部变量与全局变量
sum = 0  # 全局变量

def add(num1, num2):
    sum = num1 + num2  # 局部变量，与全局变量同名
    print("函数内局部变量 sum：", sum)
    return sum

print(add(10, 20))
print("函数外全局变量 sum：", sum)  # 全局变量未被修改

"""
修改全局变量：`global` 关键字
"""
# 函数内默认不能修改全局变量（会被解析为局部变量），需用 `global` 声明该变量为全局变量
var1 = 100  # 全局变量

def function_a():
    global var1  # 声明 var1 为全局变量
    var1 = 200  # 修改全局变量

print("修改前：", var1)  # 输出 100
function_a()
print("修改后：", var1)  # 输出 200

# 当全局变量为可变类型时，函数内不使用 global 声明，也可以对其内容进行修改，本质为传址。
def function_a():
    list1[0] = -1000
    print("list1:", list1)

list1 = [1, 2, 3]
print(list1)  # [1, 2, 3]
function_a()  # list1: [-1000, 2, 3]
print(list1)  # [-1000, 2, 3]


"""
nonlocal 关键字
内层函数修改外层嵌套函数的变量时，需用 `nonlocal` 声明。
"""
def function_outer():
    var1 = 1  # 嵌套作用域变量
    print("修改前：", var1)

    def function_inner():
        nonlocal var1  # 声明 var1 为嵌套作用域变量
        var1 = 200  # 修改嵌套作用域变量

    function_inner()
    print("修改后：", var1)

function_outer()  # 输出：修改前：1；修改后：200
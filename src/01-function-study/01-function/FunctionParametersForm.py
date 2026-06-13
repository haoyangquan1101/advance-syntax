"""
函数调用时的参数形式
"""

"""
函数调用时的参数形式
"""
# 必须参数（位置参数）
# 最基础的参数形式，调用时实参顺序需与形参一致，数量必须匹配
# 演示位置参数
def func(a, b, c):
    print(f'a:{a};b:{b};c:{c}')
    print(a, b, c)

func(1, 2, 3)  # 正确：1 传给 a，2 传给 b，3 传给 c
print("-"*30)


# 关键字参数
# 调用时通过“参数名=值”的形式传递，无需遵循形参顺序，可读性更强
# 演示关键字参数
def printInfo(name, age):
    print("姓名：", name)
    print("年龄：", age)

# 顺序可调整
printInfo(name="张三", age=18)
printInfo(age=18, name="张三")
print("-"*30)


# 默认值参数
# 定义函数给形参指定默认值，调用时若未传递该参数，则使用默认值
# 演示默认值参数
def printInfo(name, age=20):  # age 默认值为 20
    print("姓名：", name)
    print("年龄：", age)

printInfo("张三")  # 未传 age，使用默认值 20
printInfo("李四", 30)  # 传递 age=30，覆盖默认值
printInfo(age=40, name="王五")  # 结合关键字参数
print("-"*30)

# 可变参数
# - `*var_args_tuple`：接收多个位置参数，打包为元组；
# - `**var_args_dict`：接收多个关键字参数，打包为字典。
# 不定长参数
def printInfo(num, *vartuple):
    print("固定参数：", num)
    print("不定长参数（元组）：", vartuple)

printInfo(70, 60, 50)  # 输出：固定参数：70；不定长参数（元组）：(60, 50)

# 不定长参数后若有其他参数，需通过关键字传递
def printInfo1(num1, *vartuple, num):
    print("num：", num)
    print("num1：", num1)
    print("不定长参数：", vartuple)

printInfo1(10, 20, num=40)  # 正确：num 需关键字传递
print("-"*30)

# 演示 ** 不定长参数
def printInfo(num, **vardict):
    print("固定参数：", num)
    print("不定长参数（字典）：", vardict)

printInfo(10, key1=20, key2=30)  # 输出：固定参数：10；不定长参数（字典）：{'key1':20, 'key2':30}
printInfo(10, a=20, b=30)  # 输出：固定参数：10；不定长参数（字典）：{'a':20, 'b':30}
print("-"*30)

# 解包传参
def func(a, b, c):
    return a + b + c

# 解包元组
tuple1 = (1, 2, 3)
print(func(*tuple1))  # 等价于 func(1, 2, 3)

# 解包字典（key 需与形参名一致）
dict1 = {"a": 1, "b": 2, "c": 3}
print(func(**dict1))  # 等价于 func(a=1, b=2, c=3)

# 强制位置 / 关键字参数
# - `/` 前的参数必须用位置传递；
# - `*` 后的参数必须用关键字传递。
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

f(1, 2, 3, d=4, e=5, f=6)  # 正确：a、b 位置传递；e、f 关键字传递
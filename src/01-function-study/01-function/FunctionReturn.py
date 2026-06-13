"""
函数返回值
    返回值是函数执行后的结果，通过 `return` 关键字返回给调用者。
        1. `return` 可终止函数执行，后续代码不再运行；
        2. 未写 `return` 或 `return` 后无表达式，默认返回 `None`；
        3. 可返回多个值，多个值会自动打包为元组。
"""

# 基础返回值
# 求两个数的和
def add(num1, num2):
    sum1 = num1 + num2
    return sum1  # 返回求和结果

res = add(10, 20)
print("两数之和：", res)  # 输出 30

# 返回多个值
def f(a, b, c):
    return a, b, c, [a, b, c]  # 返回多个值，自动打包为元组

result = f(1, 2, 3)
print(result)  # 输出 (1, 2, 3, [1, 2, 3])

# 无返回值
def f(a, b, c):
    pass  # 无 return 语句
print(f(1, 2, 3))  # 输出 None
"""
Lambda表达式
    Lambda表达式是Python中的一种匿名函数，用于创建简洁的函数对象。
    Lambda表达式的基本语法是：lambda 参数列表: 表达式
    Lambda表达式可以有多个参数，但只能有一个表达式。
    Lambda表达式的返回值是表达式的计算结果。
"""

"""
作为参数传递
"""
# 普通函数
def operator(a, b):
    return a + b

def function(a, b, op):
    return op(a, b)

# 传递普通函数
print(function(1, 2, operator))  # 输出 3

# 传递匿名函数
print(function(1, 2, lambda x, y: x + y))  # 输出 3


"""
结合内置函数使用
匿名函数常与 `sorted()`、`map()`、`filter()`、`reduce()` 等内置函数搭配，简化代码：
"""
from functools import reduce

# 1. sorted()：按年龄排序
student_list = [{"name": "张三", "age": 36}, {"name": "李四", "age": 14}, {"name": "王五", "age": 27}]
print(sorted(student_list, key=lambda x: x["age"]))

# 2. map()：对序列元素逐一处理
map_result = map(lambda x: x * x, [0, 1, 3, 7, 9])
print(list(map_result))  # 输出 [0, 1, 9, 49, 81]

# 3. filter()：筛选非负数
filter_result = filter(lambda x: x >= 0, [-0, -1, -3, 7, 9])
print(list(filter_result))  # 输出 [0, 7, 9]

# 4. reduce()：序列元素累积相乘
reduce_result = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(reduce_result)  # 输出 120

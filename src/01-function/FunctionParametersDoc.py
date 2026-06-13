"""
函数说明文档
"""
def add(name,num1,num2):
    """
    某人计算两个数的和方法
    :param name: 计算和的人名
    :type name: str
    :param num1: 参与计算的第一个数
    :type num1: int
    :param num2: 参与计算的第二个数
    :type num2: int
    :return 两个数的和
    :rtype int
    """
    print(f"{name}在计算{num1}与{num2}的和")
    return num1 + num2

print(add("小王", 1, 2))
help(add)  # 查看说明文档

# 其他的形式  -> tuple标注返回值类型
def dog(name: str, age: (1, 99), species: '狗狗的品种') -> tuple:
    """
    返回狗狗的信息
    :param name: 名字（字符串类型）
    :param age: 年龄（1-99之间）
    :param species: 品种（字符串描述）
    :return: 包含名字、年龄、品种的元组
    """
    return (name, age, species)

# 查看注释（通过 __annotations__ 属性）
print(dog.__annotations__)
class Person:
    """人的类，包含基本属性和行为"""
    # 类属性（所有对象共享）
    home = "earth"
    age = 0

    # 构造方法（初始化实例属性）
    def __init__(self):
        self.age = 0  # 实例属性（每个对象独有）

    # 普通方法
    def eat(self):
        print("eating...")

    def drink(self):
        print("drinking...")


"""
成员引用
"""
# 访问类属性
print(Person.home)  # 输出：earth
print(Person.age)  # 报错：AttributeError: 'type' object Person has no attribute 'age'

# 访问类方法（返回函数对象）
eat_func = Person.eat
print(eat_func)  # 输出：<function Person.eat at 0x00000232C8230F40>

# 访问类说明文档
print(Person.__doc__)  # 输出：人的类，包含基本属性和行为
print("="*20)


"""
实例化
"""
# 创建对象（实例化）
p = Person()

# 访问实例属性
print(p.age)  # 输出：0

# 访问类属性（对象可共享类属性）
print(p.home)  # 输出：earth

# 调用实例方法
p.eat()  # 输出：eating...
p.drink()  # 输出：drinking...
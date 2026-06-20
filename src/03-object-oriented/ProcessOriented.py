"""
面向过程编程示例，描述人生阶段变化
"""

# 定义功能,面向过程
def grow_up(person):
    """成长"""
    person['age'] += 1
    if person['age'] <= 3:
        person['stage'] = '婴儿'
    elif person['age'] <= 18:
        person['stage'] = '少年'
    elif person['age'] <= 60:
        person['stage'] = '成年'
    else:
        person['stage'] = '老年'
    print(f"{person['name']}现在{person['age']}岁，处于{person['stage']}阶段")


def study(person):
    """学习"""
    if person['stage'] == '少年':
        print(f"{person['name']}正在学校认真学习")
    else:
        print(f"{person['name']}在人生中不断学习成长")


def work(person):
    """工作"""
    if person['stage'] == '成年':
        print(f"{person['name']}努力工作，为社会做贡献")
    else:
        print(f"{person['name']}还未到工作年龄")


def retire(person):
    """退休"""
    if person['stage'] == '老年':
        print(f"{person['name']}安享晚年，回顾人生")


# 记录数据
person = {'name': '小明', 'age': 0, 'stage': '婴儿'}

for year in range(80):
    grow_up(person)
    if person['stage'] == '少年':
        study(person)
    elif person['stage'] == '成年':
        work(person)
    elif person['stage'] == '老年':
        retire(person)

person = {'name': '小红', 'age': 0, 'stage': '婴儿'}

for year in range(80):
    grow_up(person)
    if person['stage'] == '少年':
        study(person)
    elif person['stage'] == '成年':
        work(person)
    elif person['stage'] == '老年':
        retire(person)


# 面向对象，描述事物
class Person:
    def __init__(self, name):
        """初始化人类实例"""
        self.name = name
        self.age = 0
        self.stage = '婴儿'

    def grow_up(self):
        """成长"""
        self.age += 1
        if self.age <= 3:
            self.stage = '婴儿'
        elif self.age <= 18:
            self.stage = '少年'
        elif self.age <= 60:
            self.stage = '成年'
        else:
            self.stage = '老年'
        print(f"{self.name}现在{self.age}岁，处于{self.stage}阶段")

    def study(self):
        """学习"""
        if self.stage == '少年':
            print(f"{self.name}正在学校认真学习")
        else:
            print(f"{self.name}在人生中不断学习成长")

    def work(self):
        """工作"""
        if self.stage == '成年':
            print(f"{self.name}努力工作，为社会做贡献")
        else:
            print(f"{self.name}还未到工作年龄")

    def retire(self):
        """退休"""
        if self.stage == '老年':
            print(f"{self.name}安享晚年，回顾人生")


# 使用示例
xiaoming = Person('小明')
for year in range(80):
    xiaoming.grow_up()
    if xiaoming.stage == '少年':
        xiaoming.study()
    elif xiaoming.stage == '成年':
        xiaoming.work()
    elif xiaoming.stage == '老年':
        xiaoming.retire()

xiaohong = Person('小红')
for year in range(80):
    xiaohong.grow_up()
    if xiaohong.stage == '少年':
        xiaohong.study()
    elif xiaohong.stage == '成年':
        xiaohong.work()
    elif xiaohong.stage == '老年':
        xiaohong.retire()
"""
函数参数
"""

"""
形参和实参
"""
def add(a, b):  #定义方法时：a与b是形式参数，用来占位完成函数逻辑
    print(f"求{a}与{b}的和")
    return a + b

result = add(100,200)  #调用方法时，传入的100，200是实际的数据，是实际参数
print(result)
print("-"*30)

"""
传值与传址
"""
# 传值案例
def changeInt(a):

    print(f"a的id：{id(a)}")
    print(f"函数内部修改a的值之前，a的值是：{a}")
    a = 100
    print(f"a的id：{id(a)}")
    print(f"函数内部修改a的值之后，a的值是：{a}")

b = 200
print(f"b的id：{id(b)}")
changeInt(b)
print(f"函数外部作为参数传入的b的值是：{b}")
print("-"*30)

# 传址案例
def changList(mylist):
    print(f"函数内部修改列表mlist的值之前，mlist的值是：{mylist}")
    print(f"mylist的id：{id(mylist)}")
    mylist[1] = 100
    print(f"mylist的id：{id(mylist)}")
    print(f"函数内部修改列表mlist的值之后，mlist的值是：{mylist}")

mlist = [1, 2, 3]
print(f"mlist的id：{id(mlist)}")
changList(mlist)
print(f"函数外部作为参数传入的mlist的值是：{mlist}")
print("-"*30)

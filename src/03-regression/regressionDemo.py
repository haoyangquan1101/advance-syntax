"""
递归
"""
'''
    该案例演示了求整数的阶乘
    5! = 5 * 4 * 3 * 2 *1
'''
# 不使用递归的方式
def get_factorial(num):
    res = 1 #  用于存放积
    for n in range(1,num+1):
        res *= n
    return res

print(get_factorial(5))
print("-"*20)

# 递归求阶乘
def get_factorial(n):
    return n * get_factorial(n - 1) if n > 1 else 1

print(get_factorial(5))  # 输出 120（5! = 5×4×3×2×1）
# 定义函数
def my_abs(x):
    # 利用 isinstance 检测类型
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
# print(my_abs('a'))           

# 函数返回多个值
def move(x, y):
    return x, x+y
a, b = move(10, 20)
# 返回多个值的结果其实是 tuple 类型
c = move(10, 20)
print(a, b)    
print(c)

# 函数可以携带默认参数
def add(x, y=20):
    return x+y
print(add(10))
print(add(10, 10))

# 可变参数, 通过 * 
def changeArgument(*num, **dic):
    print(num)
    print(dic)
changeArgument(1, 2, 3, {'name': 'ylz', 'age': 18})
# 字典形式传参 **    
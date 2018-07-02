L = ['jack', 'tom', 'xiaohong', 'jerri', 'red']

# 1. 切片获取元素
print(L[0:3])
# 简写方式
print(L[:3])
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
# 只写[:]就可以原样复制一个list
print(L[:])

# 切字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])   # 重复两次

 
# 2. 迭代
# for ch in 'qrqwreqwr': 
#     print(ch)

# 判断一个对象是可迭代对象, 方法是通过collections模块的Iterable类型判断：
from collections import Iterable 
print(isinstance('abc', Iterable))


# 3. 列表生成式
# print(list(range(1, 100)))
result = [x * x for x in range(1, 11)]
print(result)

resstr = [m + n for m in 'ABC' for n in 'XYZ']
print(resstr)

# 4. 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 创建一个generator，有很多种方法
# 方法一: 把一个列表生成式的[]改成()
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
# 通过遍历 generator对象, 遍历无需调用 next() 方法
for n in g:
    print(n)
# 输出处理, 多参数
print(100+200)

print('hello world')

print('233', 'hello', 'life')

print('100 + 400 =', 100+400)

# 输入处理
# name = input()
# print('your name is: ', name)

# python使用缩进进行编程
a = 100
if a >= 0:
    print('a大于等于100')
else:
    print('a不是大于等于100')

# python大小写敏感    

# 转义
print('I\'m is \"ok\"')

# ''' '''表示多行
print('''
line1
line2
line3
''')

# 布尔类型
print(3 > 2)

# python 中的占位
print('Hello, %s' % 'world')

# list 数据类型
# 索引不可以越界
listitems = ['ylz', 'job', 'tom']
print(listitems)
print(listitems[1])
print(listitems[-1])
# 末尾添加 append(); 指定添加 insert(index, '内容'); 末尾删除 pop(); 指定删除 pop(index)
listitems.append('jerry')
print(listitems)

# tuple 不可修改的元组
tupleitems= ('6666', 2333, 9999)
print(tupleitems)

# for...in 遍历list, tuple
for item in listitems: 
    print(item)
# while 循环    
sum = 0
n = 100
while n > 0: 
    sum += n
    n = n - 1
print(sum)    

# Python提供一个range()函数，可以生成一个整数序列
print(list(range(8)))
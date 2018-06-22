# GetPython
学了一下叫Python的东西~


# Python 小技巧
1. 进入Python环境, 考虑(如Mac自带Python2.x版本)多个版本, 装了Python3.x的版本, 终端运行 python3 即可

2. 退出 Python 终端环境: ctrl+d; 或者 运行 exit();

3. 终端 python 终端清屏: ctrl+l  


# Python 基础语法
### 基础一
1. Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符 

2. + 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes; 以Unicode表示的str通过encode()方法可以编码为指定的bytes
   + 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法

3. 获取字符串长度: len('abc')

4. python同c语言一样的占位(%d, %f, %s), 中间使用 % 连接
   ```
		print('Hello, %s' % 'world')
   ``` 

5. % 在 python 中转义: %%

6. Python 3的字符串使用Unicode，直接支持多语言。

7. python 设置编码为 utf-8 <br/>
   `# -*- coding: utf-8 -*-`
   
### 基础二
1. list
	Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
	+ 通过索引获取元素
	+ 索引为负数从尾部获取
	+ 末尾添加 append(); 指定添加 insert(index, '内容'); 末尾删除 pop(); 指定删除 pop(index)


2. tuple
有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

3. 条件判断
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

4. 循环遍历
	Python的循环有两种: 
	+ 一种是for...in循环，依次把list或tuple中的每个元素迭代出来
	+ 第二种循环是while循环
	
5. Python提供一个range()函数，可以生成一个整数序列
	```
	list(range(8))
	```

6. Python内置了字典：dict的支持
	```
	dict = {'key': value}
	```
	+ dict获取的方式有两种: 索引 和 get()方法
	+ 判断key是否存在 key in dict

7. set和dict类似，也是一组key的集合，但不存储value。不重复
	+ add(key)方法可以添加元素到set中
	+ remove(key)方法可以删除元素


### 基础三
1. 定义函数
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:

2. 空函数
空函数，可以用pass语句, 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来.

3. isinstance()实现数据类型检查

4. import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。

5. 定义默认参数要牢记一点：默认参数必须指向不变对象！

6. 可变参数: 仅仅在参数前面加了一个*号  


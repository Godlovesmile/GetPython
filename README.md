# GetPython
学了一下叫Python的东西~


# Python 小技巧
1. 进入Python环境, 考虑(如Mac自带Python2.x版本)多个版本, 装了Python3.x的版本, 终端运行 python3 即可

2. 退出 Python 终端环境: ctrl+d; 或者 运行 exit();

3. 终端 python 终端清屏: ctrl+l  


# Python 基础语法
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

7. python 设置编码为 utf-8
   `# -*- coding: utf-8 -*-`
   



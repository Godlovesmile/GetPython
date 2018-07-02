# ––––––––––––––1. map––––––––––– 
def fn (x):
    return x * x
res = map(fn, [1, 2, 3, 4, 5])
# print(res)
# print(list(res))

# –––––––––––––2. reduce––––––––––
from functools import reduce
def add (x, y):
    return x + y
addres = reduce(add, [1, 2, 3, 4])
print(addres)

# python 求和可以直接使用 sum()
sumres = sum([1, 2, 3, 4])
print(sumres)


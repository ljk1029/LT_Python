#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档： 数学公司使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

# math
def math_demo():
    a = abs(-20)
    print("adb:", a)
    b = max(2, 3, 1, -5)
    print("max:", b)

#generator
def generator_test():
    g = (x * x for x in range(10))
    print("generator:", next(g))
    print("generator:", next(g))
    print("generator:", next(g))
    print("generator:", next(g))
  

# 迭代器
# yield 关键字用于定义一个生成器函数generator， 
# return 'done' 存在于函数内，但它并不会被直接返回给调用者。生成器函数的返回值是一个生成器对象，而不是 'done'
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 捕获 StopIteration 异常来获得
def try_test():
    g = fib(6)
    while True:
        try:
            x = next(g)
            print('g:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break

#iter
def iter_test():
    it = iter([1, 2, 3, 4, 5])
    while True:
        try:
            x = next(it)
            print("iter:", x)
        except StopIteration:
            break

#map
def map_test():
    print("map:", list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


from functools import reduce
def fn(x, y):
    return x * 10 + y
#reduce
def reduce_test():
    b = reduce(fn, [1, 3, 5, 7, 9])
    print("reduce:", b)


def is_odd(n):
    return n % 2 == 1
#filter
def filter_test():
    print("filter:", list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))) 

#sorted
def sorted_test():
    L = ['bob', 'about', 'Zoo', 'Credit']
    print("sorted:", L)  
    print("sorted:", sorted(L))  
    L = [36, 5, -12, 9, -21]
    print("sorted:", L)  
    print("sorted:", sorted(L))  



#main
if __name__ == '__main__':
    math_demo()
    #generator_test()
    #try_test()
    #iter_test()
    #map_test()
    #reduce_test()
    #filter_test()
    #sorted_test()
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' base fuction module '

__author__ = 'ljk'


# print使用
def print_demo():
    print("hello, python")
    print('您好!, python')
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print('中文'.encode('gb2312'))
    print(len('ABC'))

# list使用
def list_demo():
    classmates = ['Michael', 'Bob', 'Tracy']
    print("list:", classmates)
    print("list:", classmates.pop())
    print("list:", classmates.pop(1))
    print("list:", classmates)
    print("list range(5):", list(range(5)))
    # 排序
    a = ['c', 'b', 'a', 'a']
    print("list init:", a)
    a.sort()
    print("list sort:", a)

# tuple使用, 不能修改一旦初始化
def tuple_demo():
    classmates = ('Michael', 'Bob', 'Tracy')
    print("tuple:", classmates)
    # 防止只有一个元素，歧义
    t = (1,)
    print("tuple:", t)

# dict使用
def dict_demo():
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print("dict:", d)
    print("dict:", d['Michael'])
    # add
    d['Adam'] = 67  
    print("dict:", d['Adam'])
    # exist
    print("dict Thomas exist:", 'Thomas' in d)
    # pop
    print("dict:", d.pop('Bob'))
    print("dict:", d)
    return d

# set使用 元素不能重复
def set_demo():
    s = set([1, 1, 2, 2, 3, 3])
    print("set:", s)
    s.add(4)
    print("set:", s)
    s.remove(3)
    print("set:", s)

# str使用
def str_demo():
    a = 'abc'
    print("str:", a)
    print("str:", a.replace('a', 'A'))
    print("str:", a)
    print("str: ABC", 'ABC'.lower())
    return a   

# type
def type_test():
    print("type:", int('123')) 
    print("type:", int(12.34))
    print("type:", float('12.34'))
    print("type:", str(1.23))
    print("type:", str(100))
    print("type:", bool(1))
    print("type:", bool(''))


# 默认值指向可变对象
def add_end_a(L=[]):
    L.append('END')
    print(L)
    return L

# 默认值指向不可变对象
def add_end_b(L=None):
    if L is None:
        L = []
        L.append('END')
    print(L)
    return L

# main
if __name__ == '__main__':
    print_demo()
    list_demo()
    tuple_demo()
    dict_demo()
    set_demo()
    str_demo()
    type_test()
    add_end_a()
    add_end_a()
    add_end_b()
    add_end_b()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' base fuction module '

__author__ = 'ljk'


# print使用
def print_demo():
    print("print测试:")
    print('您好!, python')
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print("gb2312:", '中文'.encode('gb2312'))
    print("len:", len('ABC'))

# list使用
def list_demo()->list:
    print("list测试:")
    list_name = ['Michael', 'Bob', 'Tracy']
    print("list:", list_name)
    print("list:", list_name.pop())
    print("list:", list_name.pop(1))
    print("list:", list_name)
    print("list range(5):", list(range(5)))
    # 排序
    list_a = ['c', 'b', 'a', 'a']
    print("list init:", list_a)
    print("list sort:", list_a.sort())
    return list_name

# tuple使用, 一旦初始化就不能修改
def tuple_demo()->tuple:
    tuple_name = ('Michael', 'Bob', 'Tracy')
    print("tuple:", tuple_name)
    # 防止只有一个元素，歧义
    t = (1,)
    print("tuple:", t)
    return tuple_name

# dict使用
def dict_demo()->dict:
    dict_name = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print("dict:", dict_name)
    print("dict:", dict_name['Michael'])
    # add
    dict_name['Adam'] = 67  
    print("dict:", dict_name['Adam'])
    # exist
    print("dict Thomas exist:", 'Thomas' in dict_name)
    # pop
    print("dict:", dict_name.pop('Bob'))
    print("dict:", dict_name)
    return dict_name

# set使用 元素不能重复
def set_demo()->set:
    set_num = set([1, 1, 2, 2, 3, 3])
    print("set:", set_num)
    set_num.add(4)
    print("set add:", set_num)
    set_num.remove(3)
    print("set  rm:", set_num)
    return set_num

# str使用
def str_demo()->str:
    str_a = 'abcD'
    print("str:", str_a)
    print("str:", str_a.replace('a', 'A'))
    print("str:", str_a)
    print("str:", str_a.lower())
    return str_a   

# 类型转换
def type_test():
    print("类型转换:", int('123')) 
    print("类型转换:", int(12.34))
    print("类型转换:", float('12.34'))
    print("类型转换:", str(1.23))
    print("类型转换:", str(100))
    print("类型转换:", bool(1))
    print("类型转换:", bool(''))


# main
if __name__ == '__main__':
    print_demo()
    list_demo()
    tuple_demo()
    dict_demo()
    set_demo()
    str_demo()
    type_test()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器使用
def my_decorator(func):
    def wrapper():
        print("函数调用前.")
        func()
        print("函数调用后.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# 装饰器使用
def my_log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@my_log
def log_time():
    print('2015-3-25')

# 默认值指向可变对象
def add_end_a(L=['abs'], B=None)->list:
    L.append('END')
    if B is None:
        B = []
        B.append('END')
    print("L:", L, "B:", B)
    return L

if __name__ == '__main__':
    print(__name__, ':')
    say_hello()
    log_time()
    # 默认参数调用
    add_end_a()
    add_end_a()
    add_end_a(['start'])
    add_end_a(['start'])
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
说明文档：类的使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""
from base import method_decorator as bm

# 私有变量
# 实例的变量名如果以__开头，就变成了一个私有变量private，只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.score  = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

# 继承变量
class Animal(object):
    share_para = 1
    def __init__(self, name):
        self.name = name
    def run(self):
        print('Animal is running...')
   
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog Eating meat...')

# 1、在__init__外部为类共享变量，在__init__内部为类私有变量
# 但是类共享变量，在实例后，某个对象的共享变量改变后，该对象共享变量便会独立
# 2、如 share_para 类变量共享， private_para 是私有的
# 但是类change函数调用后是对实例更改，share_para 被使用后在独立
class Parent(object):
    share_para = 1
    def __init__(self, name):
        self.name = name
        self.private_para = 10
    def change(self, com, pri = 10):
        self.share_para   = com
        self.private_para = pri
        self.display()
        return self.share_para
    def display(self):
        print( f"name:{self.name}, share:{self.share_para}, private:{self.private_para}")

class Child(Parent):
    pass


# 类测试
@bm
def class_com():
    # 私有变量测试
    bart = Student('Bart Simpson', 59)
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()

# 继承测试
@bm
def class_inherit():
    animal = Animal("Animal")
    dog    = Dog("Dog")
    animal.run()
    dog.run()
    dog.eat()
    print("isinstance:", isinstance(dog, Animal))
    print("type:", type(dog))

# 共享变量测试
@bm
def class_var():
    # 共有变量测试
    parent_a = Parent("Parent_A")
    parent_b = Parent("Parent_B")
    child = Child("Child")
    child.display()
    parent_a.display()
    parent_b.display()

    # 所有值改变
    print("All change share_para:", 2)
    Parent.share_para = 2
    child.display()
    parent_a.display()
    parent_b.display()

    # 只有parent_b值变
    print("Only change parent_b:",  3)
    parent_b.change(3, 20)
    child.display()
    parent_a.display()
    parent_b.display()

    # 只有parent_b值不变
    print("All change share_para:", 4)
    Parent.share_para = 4
    child.display()
    parent_a.display()
    parent_b.display()



# main
if __name__ == '__main__':
    class_com()
    class_inherit()
    class_var()
#-*- coding:utf-8 -*-
"""
说明文档： 字符串操作使用说明
        正则匹配使用说明

作者： ljk
日期： 2023/12/07

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2
"""

#split(":")[-1]  以:分割倒数第一元素
#strip() 去掉二端空格
#strip(“#”) 去掉二端的#号


# 打印
def string_print(pub, sub, index):
    # 连接
    print( pub + "###" + sub + "###" + "topic" + str(index))
    # 转字符
    print( f"--{pub}--{sub}")
    print( ("{}--{}").format(pub, sub))

# 去字符
def string_split():
    my_string = "Hello, World, Python"
    # 使用split方法拆分字符串
    split_result = my_string.split(',')
    # 打印拆分后的结果
    print("拆分前的字符:", my_string)
    print("拆分后的结果:", split_result)
    print("拆分后的结果[0]:", split_result[0])
    print("拆分后的结果[1]:", split_result[1])
    print("拆分后的结果[1]:", split_result[-1])

# 分割
def string_strip():
    my_string = "Hello, World#, Python"
    # 使用split方法拆分字符串
    strip_result = my_string.strip()
    # 打印拆分后的结果
    print("过滤前的字符:", my_string)
    print("过滤后的结果:", strip_result)
    strip_result = strip_result.strip('#')
    print("\'#\'过滤后的结果:", strip_result)

# 正则匹配
def string_regular(str = ' '):
    pass


# main
if __name__ == '__main__':
    pub="1234"
    sub="abcdef"
    string_print(pub, sub, 0)
    string_split()
    string_strip()
    string_regular()
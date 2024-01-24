#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
说明文档：

作者： ljk
日期:  2024/01/23

用法：
  python script.py [参数1] [参数2]

示例：
  python script.py value1 value2

功能：
  输入输出demo
"""

import argparse


# 输入参数
def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--logPath", required=True, help="Specify the log file.")
    parser.add_argument("--output", help="Specify the output path for the file.")
    args = parser.parse_args()
    print("Log file path:", args.logPath)
    print("Output file path:", args.output)
    return args

# 控制台输入
def input_demo():
    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00 前')
    else:
        print('00 后')


# main
if __name__ == '__main__':
    # 使用示例
    args = parse_input()
   
    # 输入测试
    input_demo()

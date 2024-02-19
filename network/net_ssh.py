#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ssh 功能

import sys
import subprocess


ip_add    = "127.0.0.1"
user_name = "lixiang"


def usage():
    print("用法：")
    print("  {0} ".format(sys.argv[0]))
    print("  : 登录")
    print(" ")

def ssh_remote(ip, name):
    subprocess.call(["ssh", "-l", name, ip])

usage()
#exit(0)

if __name__ == '__main__':
    ssh_remote(ip_add, user_name)
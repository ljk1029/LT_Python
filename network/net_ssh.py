#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ssh 功能

import sys
import subprocess


ip_A = "172.31.3.80"
ip_B = "172.31.3.81"


def usage():
    print("用法：")
    print("  {0} [-t]".format(sys.argv[0]))
    print("  -t  A: 登录soc A")
    print("  -t   : 登录soc B")
    print(" ")


def ssh_remote(ip):
    subprocess.call(["ssh", "-l", "liauto", ip])

usage()
#exit(0)

if len(sys.argv) >= 2 and sys.argv[1] == 'A':
    print("ssh soc A")
    ssh_remote(ip_A)
else:
    print("ssh remote B")
    ssh_remote(ip_B)
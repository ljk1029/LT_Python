#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a thread module '

__author__ = 'ljk'

from multiprocessing import Pool
import os, time, random
import threading


# 获取ID
def get_process_ID(name = 'Current'):
    # 获取当前进程号
    current_process_id = os.getpid()
    # 获取当前线程对象，并从中获取线程号（ident）
    current_thread_id = threading.current_thread().ident
    print(name, "Process ID:", current_process_id)
    print(name, "Thread  ID:", current_thread_id)

# 大量进程
def process_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 进程池创建
def process_demo():
    print('Parent process (%s).' % os.getpid())
    # 创建一个包含4个进程的进程池
    p = Pool(4)
    for i in range(5):
        p.apply_async(process_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 子进程创建
def fork_demo():
    print('Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('Child  process: (%s), parent (%s).' % (os.getpid(), os.getppid()))
        exit()
    else:
        print('Parent process: (%s), child  (%s).' % (os.getpid(), pid))
        os.wait()

# 线程函数
def thread_task():
    thread_name = threading.current_thread().name
    get_process_ID(thread_name)
    print('Thread %s is running...' % thread_name)
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s >>> %s' % (thread_name, n))
        time.sleep(1)
    print('Thread %s exit.' % thread_name)

# 线程创建
def thread_demo():
    thread_name = threading.current_thread().name
    print('Thread %s is running...' % thread_name)
    t = threading.Thread(target=thread_task, name='LoopThread')
    t.start()
    t.join()
    print('Thread %s exit.' % thread_name)


if __name__ == '__main__':
    # 放到前面防止多进程，导致多线程
    thread_demo() 
    fork_demo()
    process_demo()
    
#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/08

import psutil

print(psutil.cpu_times())
#print(psutil.virtual_memory())
print(psutil.disk_partitions())
#print(psutil.disk_partitions())
#print(psutil.disk_io_counters()) # 磁盘IO
#print(psutil.net_io_counters()) # 获取网络读写字节／包的个数
#print(psutil.net_if_addrs())    # 获取网络接口信息
#print(psutil.net_if_stats()) # 获取网络接口状态
#print(psutil.net_connections())
#print(psutil.pids())
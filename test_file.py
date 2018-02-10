#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/06

#fpath = r'D:\tmp\改革历程.txt'
with open(r'D:\tmp\改革历程.txt',encoding='UTF-8',errors='ignore') as f:
    #print(f.read())
    for line in f:
        print(line.rstrip())
#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/09

#import os
import subprocess

#out = os.popen('ifconfig')
#print(out.read())

(status,output) = subprocess.getstatusoutput('ifconfig')
print(len(output))
print(type(status))
#print((output))
#for line in output:
#	print(line.strip())

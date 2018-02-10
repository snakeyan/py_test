#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/09

import subprocess

(status,output) = subprocess.getstatusoutput('ipconfig')
print(str(status) + '\n' + str(output))
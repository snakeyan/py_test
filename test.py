#!/bin/sh/python
# -*- coding: utf-8 -*-

# author xuyan
# 2018/02/06

users = {
        'aeinstein':{
                    'first':'albert',
                    'last':'einstein',
                    'location':'princeton'
                    },
                    
         'mcurie':{
                 'first':'marie',
                 'last':'curie',
                 'location':'paris'
         }
        }

for name,info in users.items():
    print("\nUsername:" + name)
#    full_name = (info["first"] + " " + info['last'])
    
    print("\tFull name:" + (info["first"] + " " + info['last']).title())
    print("\tLocation:" + info['location'].title())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:36:04 2018

@author: shinminhsu
"""


import csv
import sys


date=sys.argv[1]
person=sys.argv[2]
oldfile=sys.argv[3]
new=sys.argv[4]

print(type(new))

#編號、級別、字彙、解釋
table=[]
title=['編號','級別','字彙','解釋']
table.append(title)


newfile=date+'_'+person+'.csv'

with open(oldfile,newline='') as csvfile:

    rows = csv.DictReader(csvfile)
    
    for i,row in enumerate(rows):
        num=row['編號']
        
        if num in new:
        
            info=[]
            info.append(row['編號'])
            info.append(row['級別'])
            info.append(row['字彙'])
            info.append(row['解釋'])
            
            table.append(info)

with open(newfile, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(table)
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 04:51:41 2018

@author: Usuario
"""
import datetime
since=datetime.datetime.strptime('2017-10-23 11:56:08', '%Y-%m-%d %H:%M:%S')
since_2=datetime.datetime.strftime(since,'%S')
print(int(since_2))
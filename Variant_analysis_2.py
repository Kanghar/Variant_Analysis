#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:40:39 2018

@author: dawid
"""
output_file = open('/home/dawid/Pulpit/data_2.txt','w')
data = []
with open('data_1.txt') as file:
    for lines in file:
        line = lines.split(',')
        line = line[0].split('|')
        line= filter(None, line)
        for ele in line:
            output_file.write(ele + ',')
        output_file.write('\n')
            
            
output_file.close()
                    
                    
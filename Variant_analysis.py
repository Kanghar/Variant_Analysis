#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:26:10 2018
gnomad.exomes.r2.1.sites.chr21.vcf
@author: dawid
"""
import time

output_file = open('/home/dawid/Pulpit/data_1.txt','w')
data = []
start = time.time()
with open('/home/dawid/Pulpit/gnomad.exomes.r2.1.sites.chr21.vcf','r') as input_file:
    while True:
        for lines in range(500):
            line = input_file.readline()
            line = line.split(';')
            for str_ in line:
                if str_.startswith('vep='):
                    print (str_)
                    output_file.write(str_)


            
output_file.close()
end = time.time()
print(end - start)
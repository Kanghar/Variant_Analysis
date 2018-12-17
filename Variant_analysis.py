#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:26:10 2018
gnomad.exomes.r2.1.sites.chr21.vcf
@author: dawid
"""
import time
file_exist = True

data = []
start = time.time()
with open('C:/Users/pkord/OneDrive/Pulpit/VA/gnomad.exomes.r2.1.sites.chr21.vcf','r') as input_file, open('C:/Users/pkord/OneDrive/Pulpit/VA/data_1.txt','w') as output_file:
    for line in input_file.readlines():
        if line[0][0] == '#':
            continue
        line = line.split('\t')
        temp = [line[i] for i in [0,1,3,4,6]]
        info = line[7].split(';')
        info[0] = info[0][len('AF='):]
        info[1] = info[1][len('AN='):]
        vep = info[-1].split(',')
        for ele in vep:
            vep_info = ele.strip().split('|')
            vep_info = [vep_info[i] for i in [1,2,3,4,5,6,22]]
            output_file.write('\t'.join(temp+info[0:2]+vep_info)+'\n')            

end = time.time()
print(end - start)

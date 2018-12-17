#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:26:10 2018
gnomad.exomes.r2.1.sites.chr21.vcf
@author: dawid
"""
import time
file_exist = True
output_file = open('/home/dawid/Pulpit/Variant_analysis_data/data_1.txt','w')
data = []
start = time.time()
with open('/home/dawid/Pulpit/Variant_analysis_data/gnomad.exomes.r2.1.sites.chr21.vcf','r') as input_file:
#with open('/home/dawid/Pulpit/Variant_analysis_data/test.txt','r') as input_file:
    while file_exist == True:
        for lines in range(500):
            line = input_file.readline()
            line = line.split(';')
            for str_ in line:
                #print(line)
                if str_.startswith('vep='):
                   # print (str_)
                    output_file.write('\n' + str_)
                elif str_.startswith('21'):
                    output_file.write(str_)
            if (line == ['']):
                file_exist = False


            
output_file.close()
end = time.time()
print(end - start)

output_file = open('/home/dawid/Pulpit/Variant_analysis_data/data_2.txt','r+')
data = []
with open('/home/dawid/Pulpit/Variant_analysis_data/data_1.txt','r') as file:
    for lines in file:
        line = lines.split(',')
        line = line[0].split('|')
        line= filter(None, line)
        if line[0].startswith('21'):
            for ele_1 in line:
                ele_1 = ele_1.split('\t')
                for ele_2 in ele_1[0:2]:
                    output_file.write(ele_2 + ',')
                for ele_2 in ele_1[3:5]:
                    output_file.write(ele_2 + ',')
                #output_file.write('\n')
        else:
            for ele in line:
                output_file.write(ele + ',')
            output_file.write('\n')
            #print(lines)     
output_file.close()
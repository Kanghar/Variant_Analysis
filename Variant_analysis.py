#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:26:10 2018
@author: dawid
"""
import time
start = time.time()
with open('/home/dawid/Pulpit/Variant_analysis_data/gnomad.exomes.r2.1.sites.chr21.vcf','r') as input_file, open('/home/dawid/Pulpit/Variant_analysis_data/data_1.txt','w') as output_file:
#with open('/media/dawid/Wirusy/Variant_analysis_data/gnomad.exomes.r2.1.sites.vcf','r') as input_file, open('/home/dawid/Pulpit/Variant_analysis_data/data_1.txt','w') as output_file:
    for line in input_file:
        if line[0][0] == '#':
            continue
        line = line.split('\t')
        temp = [line[i] for i in [0,1,3,4]]
        info = line[7].split(';')
        info[0] = info[0][len('AC='):]
        info[1] = info[1][len('AN='):]
        info[2] = info[2][len('AF='):]
        vep = info[-1].split(',')
        if line[6] == 'PASS':
            for ele in vep:
                vep_info = ele.strip().split('|')
                vep_info = [vep_info[i] for i in [1,2,3,4,5,6,22]]
                output_file.write('\t'.join(temp+info[0:3]+vep_info)+'\n')    

end = time.time()
print(end - start)

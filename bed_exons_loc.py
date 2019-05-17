import csv


with open ('bed_final.txt','r') as input_file, open ('bedtools_final_output.txt','w') as output_file:
    writer = csv.writer(output_file, delimiter='\t')
    for line in input_file:
        line = line.split('\t')
        exon_loc = round((int(line[2])-int(line[7]))/(int(line[2])-int(line[1])),1)
        if line[3] == '+':
            exon_loc = round(1 - exon_loc,1)
        list_1 = line[0]+'\t'+line[4]+'\t'+line[5]+'\t'+str(exon_loc)
        list_2 = list_1.split('\t')
        writer.writerow(list_2)



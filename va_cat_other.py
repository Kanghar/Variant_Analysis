import csv

#with open('test_file.txt','r') as input_file, open('gnomad_other.txt','w') as output_file:
with open('data_1.txt','r') as input_file, open('gnomad_prot_other.txt','w') as output_file:
    for line in input_file:
        line = line.split('\t')
        line[-1] = line[-1].strip('\n')
        if line[0] == '':
            continue
        elif line[7] == 'coding_sequence_variant' or line[7] == 'protein_altering_variant' or line[7] == 'transcript_ablation':
            writer = csv.writer(output_file, delimiter='\t')
            writer.writerow(line)
        else:
            continue

# 7 col

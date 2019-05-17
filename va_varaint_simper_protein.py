import csv
import time
start = time.time()
#with open('data_test.txt','r') as input_file, open('test_file.txt','w') as output_file:
with open('data_1.txt','r') as input_file, open('gnomad_new_cat_2.txt','w') as output_file:
    for line in input_file:
        line = line.split('\t')
        line[-1] = line[-1].strip('\n')
        variant_type = line[7].split('&')
        line[7] = variant_type[0]
        line.append(int(1))
        if line[7] == 'splice_acceptor_variant' or line[7] == 'splice_donor_variant' or line[7] == 'splice_region_variant':
            line[7] = 'splicing'

        elif line[7] == 'coding_sequence_variant' or line[7] == 'protein_altering_variant' or line[7] == 'transcript_ablation':
            line[7] = 'other'

        elif line[7] == 'inframe_deletion' or line[7] == 'inframe_insertion':
            line[7] == 'inframe_indel'
            
          
        if line[7] == 'splicing' or line[7] == 'other' or line[7] == 'missense_variant' or line[7] == 'start_lost' or line[7] == 'stop_gained' or line[7] == 'stop_lost' or line[7] == 'stop_retained_variant' or line[7] == 'incomplete_terminal_codon_variant' or line[7] == 'frameshift_variant' or line[7] == 'synonymous_variant' or line[7] == line[7] == 'inframe_indel':
            writer = csv.writer(output_file, delimiter='\t')
            writer.writerow(line)
        else:
            continue
end = time.time()
print(end - start)

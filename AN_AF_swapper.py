import csv
with open("table_AF_AN.csv", "r") as input_file, open("table_AF_AN_2.csv", "w") as output_file:
    for line in input_file:
        line = line.split('\t')
        if float(line[2]) <= 0.01:
            writer = csv.writer(output_file, delimiter='\t')
            line[-1] = line[-1].strip('\n')
            line[1] = line[1].strip('""')
            writer.writerow(line)
        elif float(line[2]) > 0.01:
            continue
    


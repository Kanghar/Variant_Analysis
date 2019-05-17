import csv

with open('test_file_A.bed','r') as input_file, open('final_A.bed','w') as output_file:
    writer = csv.writer(output_file, delimiter='\t')
    for line in input_file:
        line = line.rstrip("\n")
        line = line.split('\t')
        line[1] = line[1][:-1]
        line[1] = line[1].split(',')
        line[2] = line[2][:-1]
        line[2] = line[2].split(',')
        a = [ele1+','+ele2 for ele1,ele2 in zip(line[1], line[2])]
        exons = 0
        for cords in a:
            list_1 = []
            exons = int(exons)
            cords = cords.split(',')
            exons +=1
            exons = str(exons)
            a = line[0]+'\t'+cords[0]+'\t'+cords[1]+'\t'+line[3]+'\t'+line[4]+'\t'+exons
            list_1 = a.split('\t')
            writer.writerow(list_1)













        

        

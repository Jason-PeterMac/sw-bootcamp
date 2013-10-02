scores = [85.0, 75.0, 95.0, 110.0, 56.0]
count = 0
for i in scores:
    count += i
    
print count


line = open("uniprot_sprot.fasta")
count = 0
for string in line:
    if string.startswith('>') and 'OS=Homo sapiens' in string:
        count += 1
        
print count
line.close()

import sys
dna = sys.argv[1]
dna_dict = {'A':0, 'C':0, 'G':0, 'T':0}
dna_dict['A'] = dna.count('A')
dna_dict['C'] = dna.count('C')
dna_dict['G'] = dna.count('G')
dna_dict['T'] = dna.count('T')
dna_dict['T'] += dna.count('U')
print dna_dict
gc = (dna_dict['C'] + dna_dict['G']) / float(len(dna))*100
print "GC content: " + str(gc) + "%"


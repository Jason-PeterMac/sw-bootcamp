def base_count(sequence, base):
    # returns the number of times base X occurs
    # in the sequence
    return sequence.count(base)
    
def gc_content(sequence):
    # returns the GC content of the sequence
    return (sequence.count('C') + sequence.count('G')) / float(len(sequence))*100
    
print base_count("ACTGTGCAGTC", 'A')
print gc_content("ACTGTGCAGTC")


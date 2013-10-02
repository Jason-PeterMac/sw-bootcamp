from DNASequence import DNASequence

x = DNASequence("AAAACTGCGCGT")
print x.sequence
print x.base_count("A")
print x.gc_content()
print x.revcomp()

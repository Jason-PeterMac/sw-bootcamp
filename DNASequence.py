import string

class InvalidBaseException(Exception)
    pass
    

class NucleotideSequence:
    ''''A general nucleotide class. The class is inherited by DNASequence
    and RNASequence classes. Not for general use. Use DNASequence and
    RNASequence instead'''
    compl = ["ACTG", "TGAC"]
    valid = set("ATGC")

    def __init__(self, sequence):
        '''Input sequence should be a string,
        in all upper case letters.'''
        assert isinstance(sequence, str)
        assert len(sequence) > 0
        if set(sequence).difference(self.valid) != set():
            raise InvalidBaseException("Your input contains an invalid base(s):" + ''.join(set(sequence).difference(self.valid))
            
        self.sequence = sequence
        self.base_counts = {}
        
    def base_count(self, base):
        '''Given a base, returns the number of
        times the base occurs in this sequence.
        
        Returns an integer.'''
        assert isinstance(sequence, str)
        assert len(base) == 1
        assert base in self.valid
        if base not in self.base_counts:
            self.base_counts[base] = self.sequence.count(base)
        return self.base_counts[base]
        
    def gc_content(self):
        '''returns the GC content of the sequence
        
        Returns a float.'''
        return (self.sequence.count('C') + self.sequence.count('G')) / float(len(self.sequence))*100

    def revcomp(self):
        ''''Given a sequence, reverses that sequence and then 
        complemenents it (G's become C's, A's become T's, etc), then returns
        the new sequence.'''
        rev = self.sequence[::-1]
        rev = rev.translate(string.maketrans(self.compl[0], self.compl[1]))
        return rev
        
class DNASequence(NucleotideSequence):
    '''Extends NucleotideSequence for DNA''' 
    pass
    
class RNASequence(NucleotideSequence):
    '''Extends NucleotideSequence for RNA'''
    compl = ["ACUG", "UGAC"]
    valid = set("AUGC")

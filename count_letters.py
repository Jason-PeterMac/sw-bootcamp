import sys
import string
sent = sys.argv[1:]
sent1_lower = sent[0].lower()
sent2_lower = sent[1].lower()
set1 = set(sent1_lower)
set2 = set(sent2_lower)

valid = set(string.lowercase)
set1 = set1.intersection(valid)
set2 = set2.intersection(valid)

print "there are " + str(len(set1)) + " unique characters in the string " + sent[0]
print "there are " + str(len(set1.intersection(set2))) + " characters in common"
print "there are " + str(len(set1) - len(set1.intersection(set2))) + " characters unique to " + sent[0]
print "there are " + str(len(set2) - len(set1.intersection(set2))) + " characters unique to " + sent[1]


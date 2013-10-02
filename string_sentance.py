import sys
text = sys.argv[1:]
text.sort()
text[0] = text[0].capitalize()
text[-2] = text[-2] + " and " + text[-1] + '.'
text.pop()
string = ", ".join(text)
print string


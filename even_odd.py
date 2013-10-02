import sys
int = int(sys.argv[1])
if int % 2 == 0:
    print "even"
else:
    print "odd"


if int < 50 and int > 0:
    print "Minor"
elif int >= 50 and int < 1000:
    print "Major"
else:
    print "Severe"
    


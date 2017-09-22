#!/usr/bin/python


from operator import itemgetter
import sys

id = 0
# input comes from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    print '%s\t%s' % (id, line )
    id = id + 1
   

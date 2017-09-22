#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
        
    line = line.strip()
    # split the line into words
    try:
    	id, labels= line.split('\t', 1)
    except:
	    continue
    # increase counters
    print '%s\t%s' % (1, labels)

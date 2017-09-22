#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
count =0 
sum = 0
for line in sys.stdin:
    # remove leading and trailing whitespace
        
    line = line.strip()
    # split the line into words
    try:
    	id, labels= line.split('\t', 1)
    except:
	    continue
    sum = sum + int(labels)
    count = count + 1
print sum *1./count

#!/usr/bin/python

import sys
import re
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    word1, word2 = line.split('\t')
    if bool( re.match('Y=.+X=[a-z]+',word1)):
                
        word1 = word1.split('^')[1]
        
        word1 = word1[2:] 
        # increase counters
        print '%s\t%s' % (word1, line)


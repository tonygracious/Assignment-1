#!/usr/bin/python

import sys
import re
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    word1, word2 = line.split('\t')
    if not bool( re.match('Y=.+X=[a-z]+',word1)):
                
        
        print line


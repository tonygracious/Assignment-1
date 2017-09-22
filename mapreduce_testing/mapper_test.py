#!/usr/bin/python

import sys
import re
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into labels and text
    try :
    	id, labels, text = line.split('\t')
    except:
	    continue
    
    text = re.sub(r'[^a-zA-Z]', " ",re.sub(r'<.*>',"", text) ).split()[:-1]

    for word in text:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        word  = word.lower()
        word  = word.replace(" ","")
        print "%s\t~%s" %(word, id)



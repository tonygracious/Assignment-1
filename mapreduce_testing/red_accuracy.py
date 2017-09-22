#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = []
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py00
    word, text = line.split('\t', 1)

    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count.append( text )
    else:
        if current_word:
            # write result to STDOUT
            if len(current_count ) == 2 :
                current_count = sorted(current_count)
                if current_count[1][1:] in current_count[0].split(',') :
                    print '%s\t%s' % (current_word, 1)
		else :
		    print '%s\t%s' % (current_word, 0)
                
        current_count =[text]
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if len(current_count ) == 2 :
                    current_count = sorted(current_count)
                    if current_count[1][1:] in current_count[0].split(',') :
                        print '%s\t%s' % (current_word, 1)
		    else :
			print '%s\t%s' % (current_word, 0)                 

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

    # parse the input we got from mapper.py
    word, text = line.split('\t', 1)

    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count.append( text )
    else:
        if current_word:
            # write result to STDOUT
            if len(current_count ) >= 2 :
                current_count = sorted(current_count)
                param = current_count[0]
                if '~' not in param:
                    for i in current_count[1:]:
                        print '%s\t%s\t%s' % (current_word, i, param)
                
        current_count =[text]
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    if len(current_count ) >= 2 :
                    current_count = sorted(current_count)
                    param = current_count[0]
                    if '~' not in param:
                        for i in current_count[1:]:
                            print '%s\t%s\t%s' % (current_word, i, param)
    

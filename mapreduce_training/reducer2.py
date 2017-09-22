#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_param = ""
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, param = line.split('\t', 1)

    
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_param = current_param + ',' + param
    else:
        if current_word:
            # write result to STDOUT
            print '%s\t%s' % (current_word, current_param)
        current_param = param
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print '%s\t%s' % (current_word, current_param)

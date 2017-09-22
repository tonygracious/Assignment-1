#!/usr/bin/python

import sys
import math

h = {}
classes = {}
m= 1

f = open('class_param_large.txt', 'r')
for line in f:
    line = line.strip()
    key, value = line.split('\t')
    h[key]  = int(value)
    if ('Y=' in key) and ('X' not in key) and (key != 'Y=ANY'):
        classes[key[2:]] = 0
f.close()



classes_labels = set(classes.keys())


for line in sys.stdin:
    line = line.strip()
    for key in classes_labels :
        classes[key] = math.log( ( h['Y=' + key] + m * 1./ h['$NClass'] ) /  (h['Y=ANY'] +1*m ) )
    key, value = line.split('\t', 1)
    
    value = value.split('.')
    for v in value:
        
        word, dist = v.split('\t', 1)
        
        dist = dist.split(',')
        word_class_labels = set()
        for w in dist:
            class_value, count = w.split('\t') 
            class_value = class_value.split('=')
            class_value[2] ='ANY'
            word_class_labels.add(class_value[1][:-2] )
            classes[class_value[1][:-2]] = classes[class_value[1][:-2]] +  math.log(  ( int(count ) + m* 1./ h['$Vsize']  ) / (  h['='.join(class_value) ] + m* 1) )
        
        for class_not_word in classes_labels - word_class_labels:
            classes[class_not_word] = classes[class_not_word] + math.log(  (  m* 1./ h['$Vsize']  ) / (  h['Y=' + class_not_word + '^X=ANY' ] + m* 1) )
    
    print '%s\t~%s' %( key, max(classes, key=classes.get) )
    

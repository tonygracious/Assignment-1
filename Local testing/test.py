
import re
from collections import  defaultdict
import math

f = open('model_param.txt','r')
C = defaultdict(lambda: 0)
cls = set()
for line in f:
	key, value = line.split('\t')
	C[key] = int(value)
	if 'Y' in key and 'X' not in key and key != 'Y=ANY' :
		cls.add(key[2:])	
f.close()

q_x = 	1./C['Nsize']
q_y =   1./C['Nclass']

f =  open('/scratch/ds222-2017/assignment-1/DBPedia.full/full_test.txt', 'r')
test_size = 0
acc = 0
for article in f:
	
	try :        
        	labels, line = article.split('\t')
	except:
		continue	
	test_size = test_size + 1
	        
	labels = labels.split(',')
        labels = [label.replace(" ","") for label in labels]
            
        line  = re.sub(r'[^a-zA-Z]', " ",re.sub(r'<.*>',"", line) ).split()[:-1]
        likli = []
        for label in cls :
            prob = 0
            for word in line :
                word  = word.lower()
                word  = word.replace(" ","")
                
                prob = prob + math.log( ( C.get('Y='+label + '^X=' +word, 0) + q_x )* 1./  ( C.get('Y='+label + '^X=ANY', 0) + 1 ) ) 
            prob = prob + math.log( ( C.get('Y='+label, 0) + q_y ) * 1./ (C['Y=ANY'] + 1) )
            likli.append((label,prob))
        predict = sorted(likli, key = lambda x: -x[1])[0][0]
        acc = acc + int (predict in labels)
        
        
        
f.close()

print acc *1./test_size


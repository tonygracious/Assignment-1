

import re
from collections import  defaultdict

cls  = set()
vocab= set()

C = defaultdict(lambda: 0)

f =  open('/scratch/ds222-2017/assignment-1/DBPedia.full/full_train.txt', 'r') 

for article in f:
	try :        
        	labels, line = article.split('\t')
        except :
		continue
	C['Y=ANY'] = C['Y=ANY'] + 1
        labels = labels.split(',')
        for label in labels:
            label = label.replace(" ","")
            C['Y='+label] = C['Y='+label] + 1
            cls.add(label)
        line  = re.sub(r'[^a-zA-Z]', " ",re.sub(r'<.*>',"", line) ).split()[:-1]
        
        for word in line :
            word  = word.lower()
            word  = word.replace(" ","")
            vocab.add(word)
            for label in labels:
                label = label.replace(" ","")
                C['Y='+label + '^X=' +word] =  C['Y='+label + '^X=' +word] + 1
                C['Y='+label + '^X=ANY'] =  C['Y='+label + '^X=ANY'] + 1
        
f.close()

f = open('model_param.txt', 'w')
      
for key in C.keys():
	f.write(key+'\t'+ str(C[key]) +'\n')

f.write('Nsize\t'+ str(len(vocab)) +'\n')
f.write('Nclass\t'+str(len(cls)) +'\n')

f.close()	        



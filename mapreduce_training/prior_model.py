
import os
f = os.popen('cat class_param_large.txt | wc -l') 
L = int(f.readlines()[0])
f.close()
L = (L -1) /2 
f = os.popen('echo $\'NClass\t' + str(L)+ '\' >> class_param_large.txt')
f.close()
f = os.popen('hdfs dfs -cat /user/tonygracious/vocab_size/part-*') 
L =  int(f.readlines()[0])
f.close()
f = os.popen('echo $\'Vsize\t' + str(L)+ '\' >> class_param_large.txt')
f.close()

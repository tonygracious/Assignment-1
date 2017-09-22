#!/bin/bash

HADOOP_JAR_PATH="/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar"


hadoop jar $HADOOP_JAR_PATH \
-file "/home/tonygracious/assign1/mapper1.py" -mapper "mapper1.py" \
-file "/home/tonygracious/assign1/reducer1.py" -reducer "reducer1.py" \
-input "/user/ds222/assignment-1/DBPedia.full/full_train.txt" \
-input "/user/ds222/assignment-1/DBPedia.full/full_devel.txt" \
-output "/user/tonygracious/word_count_large" \
-numReduceTasks 2

hadoop jar $HADOOP_JAR_PATH \
-file "/home/tonygracious/assign1/mapper2.py" \
-mapper "mapper2.py" -file "/home/tonygracious/assign1/reducer2.py"  \
-reducer "reducer2.py" \
-input "/user/tonygracious/word_count_large/part-*" \
-output "/user/tonygracious/word_class_freq_large" \
-numReduceTasks 2

hadoop jar $HADOOP_JAR_PATH \
-file "/home/tonygracious/assign1/mapper_prior.py" -mapper "mapper_prior.py" \
-input  "/user/tonygracious/word_count_large/part-*"  \
-output "/user/tonygracious/class_param_large"  \
-numReduceTasks 0

hadoop jar $HADOOP_JAR_PATH \
-file "/home/tonygracious/assign1/map_key_count.py" -mapper "map_key_count.py" \
-file /"home/tonygracious/assign1/red_key_count.py" -reducer "red_key_count.py" \
-input "/user/tonygracious/word_class_freq_large/part-*" \
-output "/user/tonygracious/vocab_size" \
-numReduceTasks 1

hdfs dfs -cat "/user/tonygracious/class_param_large/part-*" > "class_param_large.txt"
python "prior_model.py"

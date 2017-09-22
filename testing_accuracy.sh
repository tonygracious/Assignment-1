#!/bin/bash

hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/mapper_id.py" -mapper "mapper_id.py" \
-file "/home/tonygracious/assign1/reducer_id.py" -reducer "reducer_id.py" \
-input "/user/ds222/assignment-1/DBPedia.full/full_test.txt" \
-output "/user/tonygracious/test_rowid" \
-numReduceTasks 1

hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/mapper_test.py" -mapper "mapper_test.py" \
-file "/home/tonygracious/assign1/reducer_test.py" -reducer "reducer_test.py" \
-input "/user/tonygracious/test_rowid/part-00000" \
-output "/user/tonygracious/test_words" \
-numReduceTasks 2 


hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/mapper_join.py" -mapper "mapper_join.py" \
-file "/home/tonygracious/assign1/reducer_join.py" -reducer "reducer_join.py" \
-input  "/user/tonygracious/word_class_freq_large/part-*"  \
-input "/user/tonygracious/test_words/part-*" \
-output "/user/tonygracious/test_words_param"  \
-numReduceTasks 2

hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/mapper_test_id_word.py" -mapper "mapper_test_id_word.py" \
-file "/home/tonygracious/assign1/reducer_test_id_word.py" -reducer "reducer_test_id_word.py" \
-input "/user/tonygracious/test_words_param/part-*" \
-output "/user/tonygracious/test_text_param"  \
-numReduceTasks 2

hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/mapper_test_id_word.py" -mapper "mapper_test_id_word.py" \
-input "/user/tonygracious/test_words_param/part-*" \
-output "/user/tonygracious/test_text_predict"  \
-numReduceTasks 0


hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/class_param_large.txt" \
-file "/home/tonygracious/assign1/map_predict3.py" -mapper "map_predict3.py" \
-input "/user/tonygracious/test_text_param/part-*" \
-output "/user/tonygracious/predict_test_data"  \
-numReduceTasks 0

hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/map_label.py" -mapper "map_label.py" \
-file "/home/tonygracious/assign1/red_label.py" -reducer "red_label.py" \
-input "/user/tonygracious/test_rowid/part-00000" \
-output "/user/tonygracious/labels_true" \
-numReduceTasks 2


hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/map_accuracy.py" -mapper "map_accuracy.py" \
-file "/home/tonygracious/assign1/red_accuracy.py" -reducer "red_accuracy.py" \
-input "/user/tonygracious/labels_true/part-*" \
-input "/user/tonygracious/predict_test_data/part-*" \
-output "/user/tonygracious/accuracy"  \
-numReduceTasks 2


hadoop jar "/usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar" \
-file "/home/tonygracious/assign1/map_agg.py" -mapper "map_agg.py" \
-file "/home/tonygracious/assign1/red_agg.py" -reducer "red_agg.py" \
-input "/user/tonygracious/accuracy/part-*" \
-output "/user/tonygracious/accuracy_sum" \
-numReduceTasks 1


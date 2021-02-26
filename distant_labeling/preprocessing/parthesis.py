# -*- coding: utf-8 -*-
# @Time    : 2019-08-02 17:47
# @Author  : Wei Peng
# @FileName: parthesis.py

import json
import sys

fin = sys.argv[1]
fout = sys.argv[2]


with open(fin, "r") as f:
    with open(fout, "w") as f1:
        line = f.readline()
        while line:
            dict = json.loads(line)
            sentences = dict["sentences"]
            for j in range(len(sentences)):
                sentence = sentences[j]
                for i in range(len(sentence)):
                    if sentence[i] == "(":
                        # print(dict["sentences"][j][i])
                        dict["sentences"][j][i] = "-LRB-"
                        # print("fweghrytger")
                    if sentence[i] == ")":
                        # print(dict["sentences"][j][i])
                        dict["sentences"][j][i] = "-RRB-"
                        # print("fweghrytger")
                    if sentence[i] == "[":
                        # print(dict["sentences"][j][i])
                        dict["sentences"][j][i] = "-LSB-"
                        # print("fweghrytger")
                    if sentence[i] == "]":
                        # print(dict["sentences"][j][i])
                        dict["sentences"][j][i] = "-RSB-"
                        # print("fweghrytger")
            # print(dict)
            json.dump(dict, f1)
            f1.write("\n")
            line = f.readline()
    f1.close()
f.close()


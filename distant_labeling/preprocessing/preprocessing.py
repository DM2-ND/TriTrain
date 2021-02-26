import json


import sys

inputname = sys.argv[1]
outputname = sys.argv[2]

with open(inputname, "r") as fr:
    with open(outputname, "w") as fw:
        i = 0
        count = 0
        for line in fr:
            if line == "":
                continue
            abstract = json.loads(line)
            sentences = abstract["sentences"]
            for sentence in sentences:
                new_dict = {}
                new_dict["clusters"] = []
                new_dict["ner"] = []
                new_dict["relations"] = []
                new_dict["doc_key"] = "distant_positive_" +str(i)
                new_dict["sentences"] = [sentence]
                i+=1
                json.dump(new_dict, fw)
                fw.write("\n")
                count+=1
                if count % 10000 == 0:
                    print("preprocess " + str(count))


    fw.close()
fr.close()

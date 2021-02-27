import json

fr = open("input/distant-machinelearning-12000.json","r")
fw = open("output/train.txt","w")
fw1 = open("output/train.dist","w")
for line in fr:
    line = json.loads(line)
    sentences = line["sentences"]
    ner = line["ner"]
    length = 0
    for sen in sentences:
        fw.write(" ".join(sen) + "\n")
        length = len(sen)
    ner_result = length * ["0"]
    for ele in ner[0]:
        start = ele[0]
        end = ele[1]
        for i in range(start, end+1):
            ner_result[i] = "1"

    fw1.write("\t".join(ner_result) + "\n")

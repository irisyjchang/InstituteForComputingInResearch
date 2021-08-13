from lexrank import LexRank
import csv
import random

dataset = []

# user
print ("---------------------------------------------------------------------------------------------------------------")
size = int(input("sample size: "))
threshold = float(input("threshold: "))
file = str(input("dataset: "))
print ("---------------------------------------------------------------------------------------------------------------")

# file
def datasetArray (file):
    with open(file) as csvfile:
        for csvline in csvfile:
            dataset.append(csvline.replace('\n',''))

# initial input
if (file == "RANDOM.csv"):
    datasetArray("AEAAE.csv")
    for row in dataset:
        lineRandom = random.choice(dataset)
        dataset.pop(dataset.index(lineRandom))
        dataset.append(lineRandom.replace('\n',''))
    with open(file,'w') as csvfile:
        csvfile.write('\n'.join(dataset))
else:
   datasetArray(file)

# lexrank
lxr = LexRank(dataset)
summary = '\n'.join(lxr.get_summary(dataset, size, threshold))

# summary output
with open("SUMMARY.txt",'w') as txtfile:
    txtfile.write(summary)
txtfile.close()

# lexrank input
scoreRank = lxr.rank_sentences(dataset, threshold, fast_power_method=False)

# lexrank output
scoreArray = []
for score in scoreRank:
    scoreArray.append(score)
scoreArray.sort(key=float, reverse=True)
count = 0
for score in scoreArray:
    if (count < size):
        count += 1
        print ('sample ' + str(count) + ": " + str(score))
print ("---------------------------------------------------------------------------------------------------------------")

# final output
num = 0
countAE = countAAE = line = 0
with open("SUMMARY.txt",'r') as txtfile:
    for txtline in txtfile:
        txtline = txtline.replace('\n','')
        with open (file) as csvfile:
            for csvline in csvfile:
                csvline = csvline.replace('\n','')
                line += 1
                if (txtline == csvline):
                    if (file == "RANDOM.csv"):
                        with open ("AEAAE.csv") as anotherfile:
                            for row in anotherfile:
                                row = row.replace('\n','')
                                num += 1
                                if (row == csvline):
                                    if (1 <= num and num <= 2000):
                                        countAE += 1
                                    else:
                                        countAAE += 1
                            num = 0
                    if (file == "AAEAE.csv"):
                        if (2000 < line and line <= 4000):
                            countAE += 1
                        else:
                            countAAE += 1
                    if (file == "AEAAE.csv"):
                        if (1 <= line and line <= 2000):
                            countAE += 1
                        else:
                            countAAE += 1
            line = 0
percentAE = str((float(countAE)/size)*100)
percentAAE = str((float(countAAE)/size)*100)
print ("AE: " + percentAE + "%" + " | AAE: " + percentAAE + "%")
print ("---------------------------------------------------------------------------------------------------------------")


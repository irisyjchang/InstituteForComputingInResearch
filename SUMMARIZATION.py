from lexrank import LexRank
import csv

dataset = []

with open("TWEET.csv") as csvfile:
    for row in csvfile:
        dataset.append(row.replace('\n',''))

size = int(input("enter sample size: "))
threshold = float(input("enter threshold: "))

lxr = LexRank(dataset)
summary = '\n'.join(lxr.get_summary(dataset, summary_size=size, threshold=threshold))

with open("SUMMARY.txt",'w') as txtfile:
    txtfile.write(summary)
txtfile.close()

scores_cont = lxr.rank_sentences(
    dataset,
    threshold=None,
    fast_power_method=False,
)
topscorearray = []
for score in scores_cont:
    topscorearray.append(score)
topscorearray.sort(key=float, reverse=True)

countlol = 0
finalscore = ""
for score in topscorearray:
    if (countlol < size):
        countlol += 1
        finalscore += (str(score) + '\n')
print(finalscore)

size = 5
threshold = 0.02

aaeCount = 0.0
aeCount = 0.0
lineCount = 0
with open("SUMMARY.txt",'r') as txtfile:
    for line1 in txtfile:
        line = line1.replace('\n','')
        print(line)
        with open ("TWEET.csv") as csvfile:
            for line2 in csvfile:
                row = line2.replace('\n','')
                lineCount += 1
                if (row == line):
                    if (1 <= lineCount and lineCount <= 2000):
                        aeCount += 1
                        #print (aeCount)
                    else:
                    #if (2000 < lineCount and lineCount <= 4000):
                        aaeCount += 1
        lineCount = 0
aePercent = str((float(aeCount)/size)*100)
aaePercent = str((float(aaeCount)/size)*100)
print ("AE: " + aePercent + "%" + " | AAE: " + aaePercent + "%")

#random


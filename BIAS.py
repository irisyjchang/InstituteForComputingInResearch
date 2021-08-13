import matplotlib.pyplot as plt
import csv
import os

array = [[],[]]

path = os.listdir("Users/irisy/Downloads/InstituteForComputingInResearch")
file1 = 'AA.csv'
file2 = 'AAE.csv'

def bias(file): 
    with open (file,'r') as csvFile:
        table = csv.reader(csvFile, delimiter = '\s+')
    for row in table:
        array[0].append(row[0])
        array[1].append(row[1])
    print (file)

for file in path:
    if file == file1:
        bias(file)
    if file == file2:
        bias(file)

plt.bar(array[0], array[1], color = 'g', width = 0.72, label = "Age")
plt.xlabel('Names')
plt.ylabel('Ages')
plt.title('Ages of different persons')
plt.legend()
plt.show()

#corpus
#token
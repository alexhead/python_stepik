import csv
import re

def func_del_pair(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

spis = []

with open("../files/Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        pattern = '2015'
        all_inclusion = re.findall(pattern, row[2])
        if len(all_inclusion) >= 1:
            #print(row)
            spis.append(row[4])


spis_change = func_del_pair(spis)
print(spis_change)

for name in spis_change:
    i = 0
    for spi in spis:
        if spi == name:
            i += 1
    print(name, i)
spis2 = []
with open("../files/Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        pattern = '0820'
        all_inclusion = re.findall(pattern, row[4])
        if len(all_inclusion) >= 1:
            #print(row)
            spis2.append(row[5])

print(spis2)









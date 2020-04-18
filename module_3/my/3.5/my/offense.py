import csv

with open("../files/Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
       for i in range(row):
          if i == 0:
              print(row[i])
       print(row)

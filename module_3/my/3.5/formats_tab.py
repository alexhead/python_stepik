import csv

with open("./files/example.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)
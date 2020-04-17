import csv

with open("./files/example.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("./files/example.csv", "a") as f:
    writter = csv.writer(f)
    for student in students:
        writter.writerow(student)

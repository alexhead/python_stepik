
with open("dataset_24465_4.txt", "r") as input_file, open("output.txt", "w") as output_file:
    x = input_file.read()
    x = x.splitlines()
    y = len(x)

    for i in range(y):
        output_file.write(x[y-1-i])
        output_file.write("\n")


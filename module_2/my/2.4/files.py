
# r (read) - открыть для чтения (по умолчанию)
# w (write) - открыть для записи, содержимое стирается
# a (append) - открыть для записи, запись ведется в конец
# b (binary) - открыть в бинарном режиме
# t (text) - открыть в текстовом режиме (поу умолчанию)
# r+ - открыть для чтения и запси
# w+ - открыть для чтения и записи, содержимое стирается

f = open("test.txt", "r")
for line in f:
    line = line.rstrip()
    print(repr(line))

x = f.read()
print(repr(x))

f.close()

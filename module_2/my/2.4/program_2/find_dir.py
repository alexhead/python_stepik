import os
import os.path
import shutil
from itertools import groupby

x = []

for current_dir, dirs, files in os.walk("."):
    if list(filter(lambda x: x.endswith('.py'), files)):
        x.append(current_dir[2:])

x.sort()
x.remove(x[0])

new_x = [el for el, _ in groupby(x)]

f = open("output.txt", "w")
for i in range(len(new_x)):
    f.write(new_x[i])
    f.write('\n')
f.close()

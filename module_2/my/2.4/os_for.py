import os
import os.path
import shutil

shutil.copy("test.txt", "test_copy.txt")
shutil.copytree("program", "program_copy")

for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
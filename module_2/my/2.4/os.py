import os
import os.path

print(os.getcwd())
print(os.listdir())

print(os.path.exists("files.py"))
print(os.path.exists("program"))

print(os.path.abspath("files.py"))

print(os.getcwd())
os.chdir("program")
print(os.getcwd())


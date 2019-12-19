from exception import BadName, greet as exc_greet

def greet():
    print("Hello Unknown")

print(greet())

print(exc_greet("Alex"))



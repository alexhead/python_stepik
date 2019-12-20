
lst = [1, 2, 3, 4, 5, 6]
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year_published': 1990
}
string = "Hello, World!"

for i in string:
    print(i)
for i in book:
    print(i)
for i in lst:
    print(i)

it = iter(book)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
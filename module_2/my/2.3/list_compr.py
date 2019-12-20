# x = [-2, -1, 0, 1, 2]
# y = [i*i for i in x if i > 0] # генератор списков
# print(y)

z = [{x, y} for x in range(3) for y in range(3) if y >= x]
print(z)

z = []
for x in range(3):
    for y in range(3):
        if y >= x:
            z.append({x, y})
print(z)

#идентчые записи

#меняем скобки получаем генератор

z = ({x, y} for x in range(3) for y in range(3) if y >= x)
print(z)
print(next(z))
print(next(z))
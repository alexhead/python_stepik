x = [1, 2, 3];

print(id(x)); # отличие идентификаторов из-за того что разные объекты
print(id([1, 2, 3])); 

# чтобы ссылались на один и тот-же объект is:

x = [1, 2, 3] 
y = x
y is x
y is [1, 2, 3]
# изменяется объект, а не перемення
x = [1, 2, 3];
y = x;
print(y is x); 
x.append(4);
print(x);
print(y);


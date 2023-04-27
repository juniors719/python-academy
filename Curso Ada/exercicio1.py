x = 4.2

y = 10

z = "42"

b = not not ((x == y or True) and ((int(z) < x*y) and (type(y) == type(int(z)))))

print(b)
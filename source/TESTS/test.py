n = [1, 2, 3]
a = set(n)
print(a)
b = a
b.add(5)
print(a)
a.clear()
a |= set(n)
print(b)

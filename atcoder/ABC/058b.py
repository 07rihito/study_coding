o = list(str(input()))
e = list(str(input()))

for i in range(len(e)):
    o.insert(i * 2 + 1, e[i])

print("".join(o))
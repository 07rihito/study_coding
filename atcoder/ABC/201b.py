n = int(input())
s = []
t = []
for i in range(n):
    a, b = input().split()
    s.append(str(a))
    t.append(int(b))

second = sorted(t)[-2]
print(s[t.index(second)])
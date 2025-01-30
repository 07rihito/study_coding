from collections import defaultdict

N, M = map(int, input().split())
cities = defaultdict(list)
for i in range(M):
    i += 1
    a, b = map(int, input().split())
    cities[a].append(i)
    cities[b].append(i)
#print(f"{cities=}")

for i in range(N):
    i += 1
    print(len(cities[i]))
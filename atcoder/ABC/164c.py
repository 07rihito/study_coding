from collections import defaultdict

N = int(input())
S = defaultdict(int)
for i in range(N):
    s = input()
    S[s] += 1

print(len(S))
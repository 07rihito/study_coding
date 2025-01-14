N = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(a, reverse=True)
alice = 0
bob = 0
for i in range(len(a_sorted)):
    if i % 2 == 0:
        alice += a_sorted[i]
    else:
        bob += a_sorted[i]

print(alice - bob)
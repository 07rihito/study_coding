n,k = map(int, input().split())

for i in range(1, k + 1):
	if n % 200 == 0:
		n = n // 200
	else:
		n = 1000 * n + 200

print(n)

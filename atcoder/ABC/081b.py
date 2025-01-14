n = int(input())
a = list(map(int, input().split()))

ans = 0
is_loop = True
while is_loop:
	for i in range(n):
		if a[i] % 2 != 0:
			is_loop = False
			break
		else:
			a[i] = a[i] // 2
	if is_loop:
		ans += 1

print(ans)

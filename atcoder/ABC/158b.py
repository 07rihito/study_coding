n, a, b = map(int, input().split())

temp = n // (a + b)
if n % (a + b) == 0:
	print(temp * a)
else:
	if a < n % (a + b):
		print(temp * a + a)
	else:
		print(temp * a + n % (a + b))


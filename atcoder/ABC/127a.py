a, b = map(int, input().split())

if 13 <= a:
	print(b)
elif 6 <= a <= 12:
	print(b//2)
elif a <= 5:
	print(0)

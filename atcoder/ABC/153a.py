h, a = map(int, input().split())

temp = h % a

if temp == 0:
	print(h//a)
else:
	print(h//a + 1)

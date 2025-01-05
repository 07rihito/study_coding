a,b = map(int, input().split())

temp = (a * b) % 2
if temp == 0:
	print("Even")
else:
	print("Odd")

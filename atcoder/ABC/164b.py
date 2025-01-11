a,b,c,d = map(int, input().split())

count = 0
while True:
	if count % 2 == 0:
        # takahashi attack
		c -= b
		if c <= 0:
			print("Yes")
			break
	else:
        # aoki attack
		a -= d
		if a <= 0:
			print("No")
			break
	
	count += 1

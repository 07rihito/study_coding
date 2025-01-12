p = int(input())

index = 1
coin = 1
ans = 0
while True:
	if p <= coin:
		coin = int(coin / index)
		index -= 1
		break
	index += 1
	coin = int(coin * index)

for i in range(index, 0, -1):
	ans += p // coin
	p = p % coin
	coin = int(coin / i)

if p == 1:
	print(1)
else:
	print(ans)

n, a, b = map(int, input().split())

def calc_sum_digit(n):
	sum_digit = 0
	while n > 0:
		sum_digit += n % 10
		n //= 10
	return sum_digit

result = 0
for i in range(1, n + 1):
	if a <= calc_sum_digit(i) <= b:
		result += i

print(result)

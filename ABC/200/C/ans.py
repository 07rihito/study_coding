n = int(input())

num_list = list(map(int, input().split()))
count = 0

for i in range(0, n):
  for j in range(i+1, n):
    if (num_list[i]-num_list[j]) % 200 == 0:
      count += 1

print(int(count))
N = int(input())


if N % 100 == 0:
  print(int(N/100))
else:
  tmp = ((N+100)/100)
  print(int(tmp))

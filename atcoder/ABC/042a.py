a,b,c = map(int, input().split())

if (a+b+c) == 17:
  count5 = 0
  if a == 5:
    count5 = count5 + 1
  if b == 5:
    count5 = count5 + 1
  if c == 5:
    count5 = count5 + 1
  
  if count5 == 2:
    print("YES")
  else:
    print("NO")
else:
  print("NO")

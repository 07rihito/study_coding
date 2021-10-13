m = int(input())

km = m / 1000
if km < 0.1:
  print("00")
elif 0.1 <= km <= 5:
  km *= 10
  ans = km % 100
  if ans < 10:
    print("0{:.1g}".format(ans))
  else:
    print("{:.2g}".format(ans))
elif 6 <= km <= 30:
  km += 50
  print("{:.2g}".format(km))
elif 35 <= km <= 70:
  tmp = (km - 30)/5
  tmp += 80
  print("{:.2g}".format(tmp))
elif 70 < km:
  print("89")
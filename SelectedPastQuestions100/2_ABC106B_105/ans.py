from typing import ValuesView


N = int(input())

if N < 1 or 200 < N:
  raise ValueError("入力された数値の範囲が適切ではありません．1以上200以下の値を入力してください．")

for i in range(1, N+1, 2):
  print(i)
  
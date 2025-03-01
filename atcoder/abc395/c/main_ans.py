#!/usr/bin/env python3
def find_shortest_duplicate_subarray(N, A):
    seen = {}
    min_length = float('inf')
    left = 0
    
    for right in range(N):
        if A[right] in seen and seen[A[right]] >= left:
            min_length = min(min_length, right - seen[A[right]] + 1)
            left = seen[A[right]] + 1
        
        seen[A[right]] = right
    
    return min_length if min_length != float('inf') else -1

# 入力処理
N = int(input())
A = list(map(int, input().split()))

# 結果を出力
print(find_shortest_duplicate_subarray(N, A))
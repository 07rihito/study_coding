#!/usr/bin/env python3
def paint_grid(N):
    # グリッドの初期化（未塗り状態を -1 とする）
    grid = [[-1] * N for _ in range(N)]
    
    # 操作を順に適用
    for i in range(1, N + 1):
        j = N + 1 - i
        if i > j:
            continue
        
        color = '#' if i % 2 == 1 else '.'  # 奇数なら黒 (#)、偶数なら白 (.)
        
        for x in range(i - 1, j):
            for y in range(i - 1, j):
                grid[x][y] = color
    
    return grid

# 結果を出力する関数
def print_grid(grid):
    for row in grid:
        print("".join(row))

# N を受け取る
N = int(input())
grid = paint_grid(N)
print_grid(grid)

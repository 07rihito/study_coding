#!/usr/bin/env python3

sx, sy, tx, ty = map(int, input().split())

ans = ""
# 1回目
ans += "U"*(ty - sy) + "R"*(tx - sx)
ans += "D"*(ty - sy) + "L"*(tx - sx)
# 2回目
ans += "L" + "U"*(ty - sy + 1) + "R"*(tx - sx + 1) + "D"
ans += "R" + "D"*(ty - sy + 1) + "L"*(tx - sx + 1) + "U"

print(ans)
#print(f"{len(ans)=}")
#print(f"{len('UURRURRDDDLLDLLULUUURRURRDDDLLDL')=}")
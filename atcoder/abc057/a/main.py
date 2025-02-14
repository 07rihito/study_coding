#!/usr/bin/env python3
import datetime

A, B = map(int, input().split())

initTime = datetime.time(hour=A)
currentTime = datetime.datetime.combine(datetime.datetime.today(), initTime)
ans = currentTime + datetime.timedelta(hours=B)

print(ans.hour)

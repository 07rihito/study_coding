s = list(str(input()))
hello_world_list = list("Hello,World!")

ans = "AC"
if len(s) == len(hello_world_list):
    for i in range(len(s)):
        if s[i] != hello_world_list[i]:
            ans = "WA"
            break
else:
    ans = "WA"

print(ans)
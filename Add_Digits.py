a=int(input())  # 38
s = 0
while a > 0: # 3 > 0
    r = a % 10 # 3
    s += r # s = 0
    a = a // 10 # 0
    if a == 0 and s > 9:
        a = s
        s = 0
print(s)
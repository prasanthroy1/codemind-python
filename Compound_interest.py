p,r,t = map(int,input().split())

A =p * (1 + r/100) ** t

print("{:.02f}".format(A))
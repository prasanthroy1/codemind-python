a=int(input())
b=int(input())
for i in range(a,b+1):
    flag = 1
    for k in str(i):
        d=int(k)
        if(d==0 or i%d!=0):
            flag = 0
            break
    if flag == 1:
        print(i, end = ' ')
            
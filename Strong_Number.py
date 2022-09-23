a=int(input())
c=1
d=0
for b in str(a):# 1
    i=int(b)
    s=1
    for k in range(c,i+1):
        s*=k#1+24+120
    d+=s
if(d==a):
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")
    
        
    
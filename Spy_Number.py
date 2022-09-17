a=int(input())
s=0
p=1
for i in str(a):
    b=int(i)
    s+=b
    p*=b
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")
    
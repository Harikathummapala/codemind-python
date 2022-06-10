x=int(input())
a=0
b=1
c=0
c1=0
for i in range(1,x+1):
    c=a+b
    a=b
    b=c
    if(c==x):
        print(True)
        break
    else:
        c1=c1+1
if c1==x:
        print(False)
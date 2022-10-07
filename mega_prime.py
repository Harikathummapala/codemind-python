x=int(input())
c=0
i=0
for i in range(1,x+1):
    if x%i==0:
        c=c+1
c1=0
c2=0
c3=0
if c==2:
    d=x
    while d>0:
        c1=c1+1
        d=d//10
    while x>0:
        r=x%10
        for i in range(1,r+1):
            if r%i==0:
                c2=c2+1
        if c2==2:
            c3=c3+1
        x=x//10
        c2=0
    if c1==c3:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")
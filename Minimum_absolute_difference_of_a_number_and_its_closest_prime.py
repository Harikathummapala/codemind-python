def prime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
a=int(input())
i=a
v=a
c1=0
c2=0
if prime(a):
    print(0)
else:
    while True:
        if prime(i):
           break
        i=i+1
        c1=c1+1
    while True:
        if prime(v):
           break
        v=v-1
        c2=c2+1
    if c1>=c2:
        print(c2)
    else:
        print(c1)
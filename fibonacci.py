n=int(input())
i=0
a=0
b=1
c=0
for i in range(1,n+1):
    print(c,end=" ")
    a=b
    b=c
    c=a+b
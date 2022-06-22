x=int(input())
c=0
c1=0
a=list(map(int,input().split()))
for i in range(0,x):
    c=0
    while a[i]>0:
        c=c+1
        a[i]=a[i]//10
    if c%2==0:
        c1=c1+1
print(c1)
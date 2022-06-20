x=int(input())
a=list(map(int,input().split()))
c1=0
d=0
for i in range(x):
    c=0
    for j in range(i+1,x):
        if a[i]==a[j]:
            c=c+1
    if c>c1:
        c1=c
        d=a[i]
    if c==c1:
        if d>a[i]:
            d=a[i]
print(d)
x=int(input())
a=list(map(int,input().split()))
k=0 
for i in range(0,x):
    c=0
    d=a[i]
    for j in range(0,x):
        if d==a[j]and i!=j:
            c=1
    if c==0:
        print(d,end=" ")
        k=k+1
if k==0:
    print('-1')
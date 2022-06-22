x=int(input())
a=list(map(int,input().split()))
b=[]
k=0
for i in range(0,x):
    c=0
    for j in range(0,x):
        if a[i]==a[j] and i!=j:
            c=1
            break
    if c==0:
        b.append(a[i])
        k+=1
        a[i]=0
if k==0:
    print(-1)
else:
    max=b[0]
    for i in range(k):
        if max<b[i]:
            max=b[i]
    print(max)
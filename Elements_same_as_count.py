n=int(input())
a=list(map(int,input().split()))
k=[]
sum=0
c=0
for i in range(n):
    if a[i]!=-1:
        c=1
        for j in range(n):
            if a[i]==a[j] and i!=j:
                c=c+1
                a[j]=-1
        if a[i]==c:
            k.append(a[i])
if len(k)==0:
    print(-1)
else:
   for i in range(len(k)):
       print(k[i],end=" ")
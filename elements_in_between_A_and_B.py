n=int(input())
c=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(n):
    if l[i]<=b and l[i]>=a:
        print(l[i],end=" ")
        c=1
if c==0:
    print(-1)
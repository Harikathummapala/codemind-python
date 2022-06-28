n,l=map(int,input().split())
a=list(map(int,input().split()))
c=0

for i in range(n):
    k=abs(a[i])
    if len(str(k))==l:
        c=c+1
print(c)
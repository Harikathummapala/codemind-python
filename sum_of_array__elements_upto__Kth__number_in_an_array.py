x=int(input())
a=list(map(int,input().strip().split()))
k=int(input())
sum=0
for i in range( 0,x):
    if a[i]<=k:
        sum=sum+a[i]
print(sum)
        
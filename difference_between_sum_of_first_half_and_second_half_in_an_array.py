x=int(input())
a=list(map(int,input().strip().split()))
k=x//2
sum=0
sum1=0
for i in range( 0,k):
    sum=sum+a[i]
for i in range(k,x):
    sum1=sum1+a[i]
l=abs(sum-sum1)
print(l)
    
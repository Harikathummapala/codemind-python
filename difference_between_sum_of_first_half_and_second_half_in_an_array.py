n=int(input())
a=list(map(int,input().split()))
k=n//2
sum1=0
sum2=0
for i in range(0,k):
    sum1=sum1+a[i]
for i in range(k,n):
    sum2=sum2+a[i]
l=abs(sum1-sum2)
print(l)
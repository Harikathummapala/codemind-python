n=int(input())
a=list(map(int,input().split()))
sum=0
k=0
for i in range(n):
    sum=sum*10+a[i]
sum=sum+1
b=[]
sum1=sum
while sum>0:
    k+=1
    sum=sum//10
for i in range(k):
    r=sum1%10
    b.append(r)
    sum1=sum1//10
for i in range(k-1,-1,-1):
    print(b[i],end=" ")
    
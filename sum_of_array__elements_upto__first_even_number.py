x=int(input())
a=list(map(int,input().strip().split()))
sum=0
for i in range( 0,x):
    if a[i]%2==0:
        break
    sum=sum+a[i]
print(sum)
        
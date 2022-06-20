x=int(input())
sum=0
import math
a=list(map(int,input().split()))
for i in range(0,x):
    y=math.sqrt(a[i])
    x=y-math.floor(y)
    if x==0:
        sum+=a[i]
print(sum)
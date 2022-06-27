x,k= map(int,input().split())
a=list(map(int,input().split()))
c=0
z=[]
for i in range(x):
    if a[i]%k==0:
        c=c+1
   
print(c)
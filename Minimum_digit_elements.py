x=int(input())
a=list(map(int,input().split()))
c=0
min=999
for i in range(x):
    if len(str(a[i]))<min:
        min=len(str(a[i]))
for i in range(x):
    if len(str(a[i]))==min:
        c=c+1
print(c)
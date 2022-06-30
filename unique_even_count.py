n=int(input())
a=list(map(int,input().split()))
k=[]
for i in range(n):
    if a[i]%2==0:
        if a[i] not in k:
            k.append(a[i])
print(len(k))
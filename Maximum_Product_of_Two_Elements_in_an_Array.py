a=list(map(int,input().split()))
i=len(a)
a=sorted(a)
print((a[i-1]-1)*(a[i-2]-1))
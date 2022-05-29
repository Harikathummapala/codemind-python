n=int(input())
a=list(map(int,input().split()))
a=sorted(set(a))
l=len(a)
if n==2:
    print(max(a))
else:
    print(a[l-3])
    
n=int(input())
a=list(map(int,input().split()))
d=sorted(a)
for i in range(n):
    print(d[i],end=' ')
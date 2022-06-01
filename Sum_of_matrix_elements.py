M=int(input())
N=int(input())
sum=0
for i in range(M):
    l=list(map(int,input().split()))
    for j in range(N):
        sum+=l[j]
print(sum)
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    k=str(abs(arr[i]))
    print(len(k),end=" ")
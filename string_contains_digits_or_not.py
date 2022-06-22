x=int(input())
for i in range(x):
    j=0
    s=input()
    for char in s:
        if char.isdigit():
            print("Yes")
            j=1
            break
    if j==0:
        print("No")
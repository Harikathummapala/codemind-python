s=input()
x=input()
c=0
for char in s:
    if char==x:
        c+=1
if c==0:
    print('-1')
else:
    print(c)
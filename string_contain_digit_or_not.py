s=input()
c=0
for char in s:
    if char.isdigit():
        c+=1
if c!=0:
    print('Contains %d digit'%c)
else:
    print("Doesn't contain digit")
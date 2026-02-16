
n=input()
c=0
for i in n:
    if ord(i)<97:
        c+=1
if c>len(n)-c:
    print(n.upper())
else:
    print(n.lower())

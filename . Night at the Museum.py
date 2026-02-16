n=list(input())
n=["a",]+n
c=0
for i in range(1,len(n)):
    if abs(ord(n[i])-ord(n[i-1]))<=12:
        c+=abs(ord(n[i])-ord(n[i-1]))
    else:
        c+=26-abs(ord(n[i])-ord(n[i-1]))
print (c)

n=int(input())
s=list(input())
c=0
i=1
while len(s)>1:
    if s[i]==s[i-1]:
        s.pop(i)
        c+=1
    else:
        i+=1
    if i>=len(s):
        break
print(c)

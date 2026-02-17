n=list(input())
n1=list(input())
j,c=0,1
for i in range(len(n1)):
    if n[c-1]==n1[i]:
        c+=1
print(c)

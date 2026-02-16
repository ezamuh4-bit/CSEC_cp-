n=int(input())
n1=list(map(int,input().split()))
d=0
c=0
for i in n1:
    if i==-1:
        if d>0:
            d-=1
        else:
            c+=1
    else:
        d+=i
print(c)

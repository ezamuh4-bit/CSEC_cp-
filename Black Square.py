m=list(map(int,input().split()))
c=0
l=list(input())
for i in l:
    c+=m[int(i)-1]
print(c)

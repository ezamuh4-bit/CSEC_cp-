
n=5
c=0
for i in range(n):
    l=list(map(int,input().split()))
    if 1 in l:
        c+=abs(2-i)
        c+=abs(2-l.index(1))
print(c)

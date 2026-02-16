
n=int(input())
s=[]
l=[]
c=0
for i in range (n):
    a,b=map(int,input().split())
    s.append(a)
    l.append(b)
for i in s:
    c+=l.count(i)
print(c)

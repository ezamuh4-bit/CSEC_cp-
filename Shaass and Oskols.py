n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(m):
    x,y=map(int,input().split())
    if x==1:
        if n==1:
            l[x-1]=0
        else:
            l[1]+=l[0]-y
            l[0]=0
    elif x==n:
        l[x-2]+=y-1
        l[x-1]=0
    else:
        l[x-2]+=y-1
        l[x]+=l[x-1]-y
        l[x-1]=0
for i in l:
    print (i)

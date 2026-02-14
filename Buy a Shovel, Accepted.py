k,r=map(int,input().split())
n=0
p=0
while n<10:
    p+=k
    if k%10==0:
        n+=1
        break
    elif (p-r)%10==0:
        n+=1
        break
    elif p%10==0:
        n+=1
        break
    else:
        n+=1
print(n)

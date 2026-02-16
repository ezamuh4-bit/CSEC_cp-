#, Accepted, #, Copy
n=int(input())
b1=""
c=0
for i in range(n):
    a,b=list(input())
    if b1==a :
        c+=1
    b1=b
print(c+1)

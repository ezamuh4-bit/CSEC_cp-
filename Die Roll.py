l=list(map(int,input().split()))
x=6-(max(l))+1
if x==1:
    print("%d/%d"%(x,6))
elif x==0:
    print("%d/%d"%(x,1))
elif x==6:
    print("%d/%d"%(1,1))
elif x==2:
    print("%d/%d"%(1,3))
elif x==3:
    print("%d/%d"%(1,2))
elif x==4:
    print("%d/%d"%(2,3))
else:
    print("%d/%d"%(5,6))

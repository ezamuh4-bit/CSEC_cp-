
n=int(input())
s=input()
a=s.count("A")
d=s.count("D")
if a<d:
    print("Danik")
elif d<a:
    print("Anton")
else:
    print( "Friendship")

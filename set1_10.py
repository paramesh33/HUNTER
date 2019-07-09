a,b=map(int,input().split())
count=0
c=list(map(int,input().split()))
d=list(map(int,input().split()))
for x in c:
    for y in d:
        if x==y:
            count=count+1
if count==b:
    print("YES")
else:print("NO")

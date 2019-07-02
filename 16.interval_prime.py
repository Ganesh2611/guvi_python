g,a=map(int,input().split())
for v in range(g+1,a,1):
    if(v>1):
        for u in range(2,v):
            if(v%u==0):
                break
        else:
            print(v,end=" ")

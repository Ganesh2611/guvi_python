var=int(input())
ke=list(map(int,input().split()[:var]))
ke.sort()
for i in ke:
  print(i,end=" ")

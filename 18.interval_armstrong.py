a,ms=map(int,input().split())
for n in range(a,ms):
  te=n
  sum=0
  while te>0:
      digit=te%10
      sum=sum+digit**3
      te=te//10
      if sum==n:
           print (n, end=' ')

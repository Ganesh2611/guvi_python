a=int(input())
s=0
temp=a
while temp>0:
   digit=temp%10
   s += digit**3
   temp//=10
if a==s:
   print("yes")
else:
   print("no")

g=int(input())
if g>1:
  for a in range(2,g):
    if g%a == 0:
      print("no")
      break
  else:
    print("yes")
else:
  print("no")

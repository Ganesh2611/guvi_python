num = input ("")
try:
   num = int(num)
   mod = num% 2
   if mod > 0:
    print("Odd")
   else:
    print("Even")
except ValueError:
   print("invalid")

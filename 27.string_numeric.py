a=input()
b=a.lstrip('-').replace('.','',1).isdigit()
if(b==True):
	print("yes")
else:
	print("No")

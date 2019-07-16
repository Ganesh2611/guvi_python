sub1=int(input("Mark of Maths:"))
sub2=int(input("Mark of Tamil:"))
sub3=int(input("Mark of Science:"))
sub4=int(input("Mark of Scocial:"))
sub5=int(input("Mark of English:"))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
if avg  <= 100:
    print("Passing grade of:")

    if avg >=90:
        print("A")

    elif avg >=75:
        print("B")

    elif avg >=60:
        print("C")

    elif avg >= 50:
        print("D")

else:
    print("Failing grade")

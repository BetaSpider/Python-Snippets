n1=int(input("Enter the 1st number"))
n2=int(input("Enter the 2nd number"))
n3=int(input("Enter the 3rd number"))
if n1<n2 and n1<n3:
    print(n1,"is the smallest number")
elif n2<n3 and n2<n1:
    print(n2, "is the smallest number")
else:
    print(n3, "is the smallest number")




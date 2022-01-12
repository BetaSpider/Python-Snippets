str=input("enter the string")
print("The string is", str)
rev_str=str[::-1]
if str==rev_str:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome ")
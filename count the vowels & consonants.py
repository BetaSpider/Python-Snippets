#check the count of vowels &consonants in the given #string

str=input("enter the string")
str2="AaEeIiOoUu"
v,c=0,0
for i in str:
	if i in str2:
		v+=1
	else:
		c+=1
print("There are {} vowels and {} consonants in the given string".format(v,c))




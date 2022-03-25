import random
import string
#packages for importing for running the program 
str1=string.ascii_lowercase
str2=string.ascii_uppercase
str3=string.digits
str4=string.punctuation
# creating the type of characters are required for the program
plength=int(input("Enter the length of Password: "))
s=[]
#creating a list for storing characters 
s.extend(list(str1))
s.extend(list(str2))
s.extend(list(str3))
s.extend(list(str4))
# Extending lists by joining all the strings
print('Your Password: ',end='')
print(" ".join(random.sample(s,plength)))




punctuations = '!()-[]{};:""\,<>./?@#$%^&*_~! **'
# To take input from the user
my_str = input("Enter Your String: ")

# remove punctuation from the string

no_punctuation =" " #providing a null string

for char in my_str:
  if char not in punctuations:
    no_punctuation = no_punctuation + char

#c
# display the unpunctuated string 
print (no_punctuation)
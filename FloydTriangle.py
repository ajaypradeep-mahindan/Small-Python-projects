#program for Floyd's triangle'


number=int(input("Enter the number of rows: "))

#clcoding.com
#num means first number and i means no of elements in a row
num = 1 ;m = 0

while m< number:
    n = 0
    while n<m+1:
        print(num, end=" ")
        num = num+1
        n = n+1
    print()
    m=m+1
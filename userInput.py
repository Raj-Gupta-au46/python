# how to take user input in python 
b= input()
print(b)
a =input("Enter your name :")
print("My name is ", a)

# logical problem
x=input("enter first number")
y=input("enter second  number")
print(x+y) 
# if we give input in x = 100 , y = 12 then in print function the output will be 10012 because it take x and y value as 
# as string so it is going to concat them
#  so for adding two number givin by user be are going to use typecasting 
print(int(x)+int(y))
# this give correct value 112

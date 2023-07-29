# # string 
# name="Raj"
# friend="Harry"
# print(name[0]) 
# #indexing name[0] = R , name[1]=a , name[5] = index error
# print(name,friend)
# apple = f'hi {name} how are you and your {friend}'
# print(apple)

# # multiple line string

# intro='''
# hi  i am raj
# how r u guys
# hope u r doing well
# ohk bye
# '''
# print(intro)

# # for finding all in index of into string  , so we use for loop

# for character in intro:
#     print(character)

# string slicing 

name = "Rishabh , Aman , Vaibhav "
# what is i want only Rishabh character
#  how to find the length of a string , we use len function 
length= len(name)
print(length)

# what if i want only rish so for this thing we use slicing 
print(name[0:4])
print(name[1:7])


# methods in string 
# string are immutable


a="!!Harry !!!!"
print(len(a))  
# gives length of string
print(a.upper())
# change all character to upper case  it it gives us new string does not change a
print(a.lower())
# change all character to lower case  it it gives us new string does not change a
print(a.rstrip("!"))
# remove all the marks but it does not remove from start
print(a.replace("Harry","Raj"))
# it replace all Harry into raj
print(a.split(" "))
# it give us a list from where space are found in string and give us data in array
blogHeading= "introduction tO python"
print(blogHeading.capitalize())
# capitalize first letter and correct the the all string  if all letter are in correct form it gives us error
str= "welcome a human to is to string string "
print(len(str))
print(str.center(50))
# it gives string in center
print(str.count("string"))
# give us how many time  word happen in string
print(a.endswith("!!!"))
# it tell our string ends with !!! if yes then true unless it give us false
print(str.find("to"))
# it tell if to is present or it give only first to index 
# print(str.index("ishh")) this give use error if not find 




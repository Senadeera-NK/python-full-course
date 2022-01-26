# print('hello world')
# print("it's really good")


#-----variables in python-------#
#---data types---#
first_name = 'Nanduni' #string  -> series of characters(''/"")
last_name = 'Kaveesha'
full_name = first_name + last_name
print("Hello "+first_name)
print(type(first_name))  #to check the data type

age = 23 # int -> a whole number
age = age + 1 
age += 1
print(age)
print('age is '+str(age))#can't use different data type in one print

height = 250.5 #float -> floating point number (a decimal number)
print('height is '+str(height))

human = True #boolean -> True /False (very useful in if statement)
print('Am I a human? '+str(human)) #using string concatenation 

#four basic data types: booleans, strings, integers, floats


#------------multiple assignments--------------> assigning multiple variables in one line#

name, age, attractive = 'Nanduni',22,True
# spongeBob,patrick,sandy = 34 #they all are same age


#-----------few useful methods for strings-----------#
nameString = "Nanduni"
print(len(nameString)) #no of characters
print(nameString.find('a'))#find the index of specified character
print(nameString.capitalize())#only capitalizing the first letter
print(nameString.upper())#making all uppercase
print(nameString.lower())#making all lower case
print(nameString.isdigit())#if string contains bunch of numbers it returns True
print(nameString.isalpha())#to check if string only contains alphabetical letters
print(nameString.count("a"))#to count how many specific character exist
print(nameString.replace("a","o"))#replacing "a" with "o"
print(nameString *3)#a useful feature


#--------------------type casting(ability to convert a data type to another data type)-------------#
x = 1 #integer
y = 2.34 #float
z = "99" #string

#converting to integer
print(int(y)) #only a temperory change
y = int(y) #permenant change
z = int(z)
print(z * 8)

#converting to float
x = float(x)
print(x)

#converting to string
y = str(y)
print("y is "+y)


#----------------accept user inputs------------------#
# user_name = input('what is your name?: ') #this is string
# print('Hello '+user_name)

# user_age = int(input('how old are you?: ')) #cast them to int() or float() to use them as integers/floats
# user_age += 1
# print("you are "+str(user_age)+" years old")

# user_height = float(input('how tall are you?: '))
# print('you are '+str(user_height)+'cm tall.')


#----------useful functions related to numbers------------#
import math
pi = 3.14
x = 1
y = 4
z = 5
print(round(pi))#rounding
print(math.ceil(pi))#roudning a number up --> using ceil()
print(math.floor(pi))#rounding a number down --> using floor()
print(abs(pi))#absolute value of number --> how far the number away from zero
print(pow(pi,2))  #power --> raise a number to a given power number ex: pi * pi
print(math.sqrt(pi)) #getting the square root of a number
print(max(x,y,z))#max --> getting the largest value
print(min(x,y,z))#max --> getting the smallest value


#-----------strings slicing(useed to create a substring by extrcting elements from another string)--------------#
#[start:stop:step]
name_slice = "Nanduni Kaveesha"

first_name_slice = name_slice[0:8] #stopping index's character won't print....step:1 by default
print(first_name_slice)

last_name_slice = name_slice[8:]#or [8:16]
print(last_name_slice)

funky_name_slice = name_slice[::2]
print(funky_name_slice)

reversed_name_slice = name_slice[::-1] #reversing a name
print(reversed_name_slice)

website_slice = "https://google.com"
website_slice2 = "https://wikipedia.com"
webSite_slice_1 = slice(8,-4) #can use negative and positive indexing combination
print(website_slice[webSite_slice_1])
print(website_slice2[webSite_slice_1])


#-------------if/ifelse statements-----------------#
# age = int(input('how old are you? '))

# if age ==100:#comparison operator for equality is '=='
#   print('you are a century old')
# elif age < 0:
#   print("you haven't born yet")
# elif age >= 18:
#   print('you are an adult')
# else:
#   print('you are a child')

#---------logical operators(and,or,not)----------------#
temp = int(input('what is the temperature outside? '))

#and -> to check if two or more conditions are true or false/checking certain range
if (temp >= 0 and temp <= 20):
  print('temperature is good today!!!, run away !!!')
if(temp < 0 or temp > 30):
  print('temperature is bad !!!, die inside !!!')

#not -> flipped it to true -> false / false -> true

  










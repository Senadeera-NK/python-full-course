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
from os import utime
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
# temp = int(input('what is the temperature outside? '))

#and -> to check if two or more conditions are true or false/checking certain range
# if (temp >= 0 and temp <= 20):
#   print('temperature is good today!!!, run away !!!')
# if(temp < 0 or temp > 30):
#   print('temperature is bad !!!, die inside !!!')

#not -> flipped it to true -> false / false -> true


#----------while loop(a statement that willexecute it's block of code as long as it's conditions remains true)----#
# name_while = None
# while not name_while:
  # name_while = input('enter your name: ')

# print('hello '+name_while)
  

#---------forloops(a statement that will execute a block of code limited, defined amount of time)----------#

# for i in range(10): #works 10times(0-9)
#   print(i+1)

# for i in range(50,100): #first number inclusive, second number desclusive (50-99)
#   print(i)

#   #(start,end,step)
#   for i in range(50,100,2):
#     print(i)

#   for i in "Nanduni Kaveesha":
#     print(i)


#---------count down to 10 - 0 after that a message-----#
# import time

# for seconds in range(10,0,-1):
#   print(seconds)
#   time.sleep(1) #program waits for 1 second
# print("happy new year !")


#----------nested loops-> (one loop inside another loop)the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"-------#

# rows_nested = int(input('how many rows? '))
# columns_nested = int(input('how many columns? '))
# symbol_nested = (input('enter a symbol to use? '))


# for i in range(rows_nested):
#   for j in range(columns_nested):
#     print(symbol_nested, end="")
#   print()


#-----------loop control statements(change loop execution from its normal sequence)-------------#

#break -> use to terminate the loop entirely
# while True:
#   name = input('enter your name: ')
#   if name != "":
#     break

#continue -> skips to the next iteration of the loop
# phone_number = "123-345-5656"
# for i in phone_number:
#   if i == "-":
#     continue
#   print(i, end="") #end="" -> to print all items in one line

#pass -> does nothing, acts as a placeholder
# for i in range(1,21):
#   if i == 13:
#     pass
#   else:
#     print(i)


#-------------lists-->stores multiple items within a single variable------------------#

food =['pizza','pineapple','burger','noodles','hotdog','spaghetti']
print(food) #printing all the list
print(food[0]) #getting a one specific number using it's index

food[0] = 'sushi'#updating/changing a specific index's item

for x in food:
  print(x)


#--------useful functions of list----------------#
food.append('ice cream') #adding an item at the end of list
food.remove('sushi') #removing an item
food.pop() #removing the last element
food.insert(0,'banana') #insert a value to an specific index
food.sort() #sorting the list alphabetically
food.clear() #removing all the elements of a list


#-----------2D lists(mulideminetional list)-> a list of lists------------#
drinks = ['coffee','soda','tea']
dinner = ['pizza','burger','sushi']
desserts = ['ice cream','cake']

food = [drinks, dinner, desserts]#adding all list to one list
print(food)
print(food[0][0])  #accessing the first list's first element


#---------tuples->(collection ordered and unchangeable used to group related data)-------------#
student = ("nanduni",21,"female")
print(student.count("nanduni")) #to get how many times an item appears
student.index("female") #to find the index of a certain value

for x in student:
  print(x)

if "nanduni" in student:
  print("nanduni is here")


  #-------------set->collection is unordered, unindexed, no duplicate values-----------#
  #**set is faster than list to check an item's existence, and it doesn't allow duplication
#   utensils = {"fork","spoon","knife"}
  
# utensils.add("napkin") #adding items
# utensils.remove("fork") #removing element
# utensils.clear()#removing all items

# dishes = {"bowl","plate","cup","knife"}
# utensils.update(dishes) #dishes adding to utensils
# dinner_table = utensils.union(dishes)

# # print(dinner_table)

# print(utensils.difference(dishes)) #print what utensils has that dishes doesnt

# print(utensils.intersection(dishes)) #prints what they both have in common


#---------dictionaries -> changeable, unordered, unque key:value pairs----------#
capitals = {'USA':'Wahington DC','India':'New Delhi','China':'Beijin','Russia':'Moscow'}
print(capitals['USA']) #printing the value of the mentioned key
print(capitals.get('Germany')) #to check if specific key exists in a dictionary
print(capitals.keys()) #to get only the keys
print(capitals.values()) #to get only the values
print(capitals.items()) #to get all items(keys and values)

capitals.update({'Germany':'Berlin'}) #adding a new item
capitals.update({'USA':'Las Vegas'}) #updating an existing item
capitals.pop('China') #to remove key and value of mentioned item
capitals.clear() #to remove all items of the dictionary

for key, value in capitals.items():
  print(key, value)


#------------index operator [] = give access to sequence's element (str, list, tuples)-----------#

name = "nanduni Kaveesha"

# if(name[0].islower()):
#   name = name.capitalize()

#creating substrings
first_name_subs = name[:7].upper()
print(first_name_subs)

last_name_subs = name[8:].lower()
print(last_name_subs)

last_character = name[-1]
print(last_character)
print(name)


#---------------functions -> a block of code which is executed only when it is called-------#
def hello(first_name, last_name, age): #declaring the function
  print('Hello bitch! '+first_name+" "+last_name)
  print('you are '+str(age)+'years old')

hello("Nanduni","Kaveesha",21) #calling the function
hello("dude","bro",12)

name_func = "www"
hello(name_func, name_func,23)











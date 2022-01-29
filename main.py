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


#--------return statement->functions send python values/objects back to the caller. these values/objects are known as the function's return value--------------#
def multiply(number1, number2):
  return number1 *number2


#------keyword arguments-->>arguments preceded by an identifier when we pass them to a function the order of the argument doesn't matter, unlike positional arguments python knows the names of the arguments that our functions receives------------#
def hello_positional_arguments(first,second,last):
  print('Hello '+first+" "+second+" "+last)

hello_positional_arguments(last='Nanduni',second='Kaveesha',first='Senadeera')

def hello_keyword_arguments(first1,second2,third3):
  print('Hello '+first1+' '+second2+' '+third3)

hello_keyword_arguments(first1='Nanduni',third3='Senadeera',second2='Kaveesha')


#---------nested function calls-->function calls inside of another function calls--innermost function calls are resolved first returned value is used as argument for the nested outer function----------------#

# num = input('enter a whole positive number: ')
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input('Enter a whole positive number: ')))))


#variable scope->the region that a variable recognized, only avaialable in the region created (global/local can be created too)-------#

name_scope = 'bro' #global scope
def display_name_scope():
  name_scope='code' #local scope(only inside of the function)
  print(name_scope)

display_name_scope()
print(name_scope) #can't access,out of created region


#--------args parameter -->>a parameter that will pack all arguments into a tuple, usefil so that a function can accept a varying amount of arguments-------#
def add_args(*args): # '*'is important it does tha packing as the tuple 'args' name is changeable
  sum = 0
  stuff = list(args) #casting to a list
  stuff[0]=0 #tuples can't be updated that's why it cast into a list
  for i in stuff:
    sum +=i
  return sum

print(add_args(1,2,3,4,5))


#------kwargs(keyword arguments)-->>a parameter that will pack all arguments into a dictionary---------------#

def hello_kwargs(**kwargs): #'**' is essential, it declares a dictionary
  print("Hello ", end="")  #dictionary name['key name']
  for key,value in kwargs.items():
    print(value, end=" ")
  print()

hello_kwargs(title="Mr.",first='Nanduni',last='Kaveesha',middle='Senadeera')


#----------str.format() method-->>method available to string(optional), gives user more about the output------------#
animal = 'cow'
item = 'moon'
# print('The '+animal+' jumped over the '+item)
print('The {} jumped over the {}'.format(animal,item)) #positional arguments
print('The {1} jumped over the {0}'.format(item,animal)) #positional arguments
print('The {animal1} jumped over the {item1}'.format(animal1='cow',item1='moon')) #keyword arguments

text_format = 'The {} jumped over the {}'
print(text_format.format(animal,item))

name_format = 'Nanduni'
print('Hello my name is {}'.format(name_format))
print('Hello my name is {:10}. nice to meet you'.format(name_format)) #':10'-->> no of spaces after the name displayed
print('Hello my name is {:<10}. nice to meet you'.format(name_format))#to add spaces after name
print('Hello my name is {:>10}. nice to meet you'.format(name_format))#to add spaces before name

number_format = 1.2344
print('the number pi is {:.2f}'.format(number_format)) #2f-->>to display only first two digits after the decimal(f -> floats)

number_format2 = 1000
print('the number is {:,}'.format(number_format2))#adding ',' after the first digit
print('the number in binary is {:b}'.format(number_format2))#to get the binary representation of the number
print('the number in octal is {:o}'.format(number_format2))#to get the octal representation of the number
print('the number in hexadicimal is {:x}'.format(number_format2))#to get the hexadecimal representation of the number
print('the number in scientific notation is {:e}'.format(number_format2))#to get the scientific notation representation of the number


#-----------methods using 'random'-------------#
import random

x_random = random.randint(1,6) #to get a number between 1 and 6
print(x_random)

y_random = random.random() #to get a floating number
print(y_random)

myList_random = ['rock','paper','scissor']
z_random = random.choice(myList_random) #to get a random item from a list
print(z_random)

cards_random = [1,2,3,4,5,6,7,8,9,'J','K','Q']
random.shuffle(cards_random) #to shuffle a list or other collection
print(cards_random)


#------------------exception handling--------------------#
#---exception-->>is an event detected during execution which  interrupt the flow of the program-----------#
# try:
#     numerator_exception = int(input('enter a number to divide: '))
#     denominator_exception = int(input('enter a number to divide by: '))
#     result_exception = numerator_exception/denominator_exception
# #first catch specific exceptions, then catch the normal exception
# except ZeroDivisionError as e: #'as e'-->>to print the exception that displays by the python(optional)
#   print(e)
#   print("you can't divide by zero, idiot")
# except ValueError as e:
#   print(e)
#   print("Enter only numbers please asshole")
# except Exception as e:
#   print(e)
#   print('something went wrong')
# else: #optional
#   print(result_exception)
# finally:#with or without exception always, finally block gets executed ex:to close files which are opened
#   print('this will always execute !!!')


#-------------basic file detections--------------------#
# import os

# path ="D:\\Program Files\\python full course\\python-full-course\\text.txt" #if you have backslash '\' in file path, use '\\' double backslash(that's the escape sequence for a backslash string)
# if os.path.exists(path): #---checking file's existence---#
#   print('that location exist !!!')
#   if os.path.isfile(path): #---checking if it's a file--#
#     print('this is a file')
#   elif os.path.isdir(path): #---checking if it's a folder--#
#     print('this is a directory')
# else:
#   print('that location doesnt exist !!!')


# #------------------reading a file----------------------#
# try:
#     with open('text2.txt') as file: #this closes file automatically

#     #doesnt need if files on project folder or else input the path ex'D:\\Program Files\\python full course\\python-full-course\\text.txt'
#       print(file.read())
# except FileNotFoundError:
#   print('file was not found') 
# print(file.closed) #to check if file is closed


# #---------------writing files-------------------------#
# text_write = 'yoooooooooooo\nThis is some text\nHave a good one:\n' #'\n'-->>causing a new line
# with open('text-writing.txt','w') as file_writing:
#    file_writing.write(text_write)

# #----to append some text----#
# text_write2 = 'have a nice day! see ya(appending text)'
# with open('text-writing.txt','a') as file_writing:
#   file_writing.write(text_write2)


# #-------------copying files---------------------------#
# import shutil
# #3 ways
# #1.copyfile() = copies contents of a file
# #2.copy() = copyfile() + permission mode + detimation can be a directory
# #3.copy2() = copy() + copies metadata (file's creation and modification times)

# shutil.copyfile('text2.txt','copy.txt') #(src, destination) #if its not on project directory, name the location--------'copy.text' creating automatically

# #copy() and copy2() are same


# #--------------move files/folders-------------------------------#
# import os
# source_move = "move.txt" #if some place else give the path
# destination_move = "D:\\Program Files\\moved.txt" #can rename the file's name

# try:
#   if os.path.exists(destination_move):
#     print('theres already a file there')
#   else:
#     os.replace(source_move,destination_move) #moving the file
#     print(source_move+ ' was moved')
# except FileNotFoundError:
#   print(source_move+' was not found')


#-------------delete files----------------------#
import os

path='delete file.txt'

#exception handling is exceptional
try:
  os.remove(path) #insert the file path if it's not in project repository
except FileNotFoundError:
  print('That file was not found')

#--os.remove() function does not remove empty folders
path_delete = 'empty delete folder'
try:
  os.remove(path_delete)

  #to remove empty folders
  os.rmdir(path_delete)
except PermissionError:
  print('you do not have permission to delete that')
else:
  print(path_delete+' folder is deleted')

#--os.rmdir() function does not delete not empty folders
path_folder_delete = 'not empty folder'

try:
  os.rmdir(path_folder_delete)
except OSError:
  print('you cannot delete that using that function')

#shutil.rmtree() ->to delete not empty folders
import shutil
try:
  shutil.rmtree(path_folder_delete) #this will delete the folder including all the includes
except OSError:
  print('you cannot delete that using that function')
else:
  print('folder is deleted')


  #----------modules-->>a file containing python code, may contain functions, classes, etc. used with modular programming, which is to seperate a program into parts.--#
import messaages_modules as msg #module file name

#-----another way to import modules----#
# from messaages_modules import hello_modules, bye_modules
# from messaages_modules import * #to import all function

msg.hello_modules()#using a function from that imported module
msg.bye_modules()

#to populate all the modules that available for the file
# help('modules')


#----------basic game--->>rock, paper, scissor--------#
# import random

# while(True):
#   choice_rps = ['rock','paper','scissor']
#   computer_rps_choice = random.choice(choice_rps)

#   player_rps_choice = None

#   while player_rps_choice not in choice_rps:
#     player_rps_choice = input('rock, paper or scissor?: ').lower()

#   if player_rps_choice == computer_rps_choice:
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('Tie !!!')
#   elif player_rps_choice == 'rock':
#     if computer_rps_choice == 'paper':
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('you lose !!!')
#     if computer_rps_choice == 'scissor':
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('you win !!!')
#   elif player_rps_choice == 'scissor':
#     if computer_rps_choice == 'paper':
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('you win !!!')
#     if computer_rps_choice == 'rock':
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('you lose !!!')
#   elif player_rps_choice == 'paper':
#     if computer_rps_choice == 'rock':
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('you win !!!')
#     if computer_rps_choice == 'scissor':
#       print('computer : ',computer_rps_choice)
#       print('player : ',player_rps_choice)
#       print('you lose !!!')
  
#   play_again = input('play again(yes/no): ')
#   if play_again != 'yes':
#     break
# print('Bye !')


#------------check basic quiz game.py------------------#
#-----------check poop.py for (python object oriented programming)-------------#
from poop import Car

#in python we do not have to pass 'self' that automatically has done for us
car_1 = Car('Chevy','Corvette',2021,'Blue')
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

car_2 = Car('ford','mmustang',2022,'red')
car_2.drive()
car_2.stop()
#class-->> can function as a blue print to create objects, we can assing attributes, methods, innit method's arguments can pass in when creating an object


#------------basics of class variables-------------------#
#-----difference between class variables and instance variables----#
car_1_class = Car('Chevy','Corvette',2021,'Blue')
car_2_class= Car('ford','mmustang',2022,'red')

car_1_class.wheels = 2 #accessing class variables using it's object

Car.wheels =2 #accessing class variables using class

print(car_1_class.wheels)
print(car_2_class.wheels)


#-------------------inheritence------------------------#
#---means classes can have childrens and it  gives all(attributes,methods) parents have to children---#
#----each child classes have thier own things(attributes,methods) too---#
#----------check animals.py for more-----------#


#-----------multilevel inheritence =>> when a derived(child) class inherits another derived(child) class------#

#----like a family tree-->>inhert from grand parents to parents to childrens----#
class Organism:
  alive = True

class Animal(Organism):
  def eat(self):
    print('this animal is eating')

class Dog(Animal):
  def bark(self):
    print('this dog is barking')

dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()


#------------------mutiple inheritence-->>when a child class is derived from more than one parent class------#

#-----as an example some animals can be a prey or predator differs from situation to situation------#
class Prey:
  def flee(self):
    print('this animal flees')

class Predator:
  def hunt(self):
    print('this animal is hunting')

class Rabbit(Prey):
  pass
class Hawk(Predator):
  pass
class Fish(Prey,Predator):
  pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()

#fishes can be flee and hunt
fish.flee()
fish.hunt()
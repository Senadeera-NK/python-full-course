# print('hello world')
# print("it's really good")


# #-----variables in python-------#
# #---data types---#
# first_name = 'Nanduni' #string  -> series of characters(''/"")
# last_name = 'Kaveesha'
# full_name = first_name + last_name
# print("Hello "+first_name)
# print(type(first_name))  #to check the data type

# age = 23 # int -> a whole number
# age = age + 1 
# age += 1
# print(age)
# print('age is '+str(age))#can't use different data type in one print

# height = 250.5 #float -> floating point number (a decimal number)
# print('height is '+str(height))

# human = True #boolean -> True /False (very useful in if statement)
# print('Am I a human? '+str(human)) #using string concatenation 

# #four basic data types: booleans, strings, integers, floats


# #------------multiple assignments--------------> assigning multiple variables in one line#

# name, age, attractive = 'Nanduni',22,True
# # spongeBob,patrick,sandy = 34 #they all are same age


# #-----------few useful methods for strings-----------#
# nameString = "Nanduni"
# print(len(nameString)) #no of characters
# print(nameString.find('a'))#find the index of specified character
# print(nameString.capitalize())#only capitalizing the first letter
# print(nameString.upper())#making all uppercase
# print(nameString.lower())#making all lower case
# print(nameString.isdigit())#if string contains bunch of numbers it returns True
# print(nameString.isalpha())#to check if string only contains alphabetical letters
# print(nameString.count("a"))#to count how many specific character exist
# print(nameString.replace("a","o"))#replacing "a" with "o"
# print(nameString *3)#a useful feature


# #--------------------type casting(ability to convert a data type to another data type)-------------#
# x = 1 #integer
# y = 2.34 #float
# z = "99" #string

# #converting to integer
# print(int(y)) #only a temperory change
# y = int(y) #permenant change
# z = int(z)
# print(z * 8)

# #converting to float
# x = float(x)
# print(x)

# #converting to string
# y = str(y)
# print("y is "+y)


# #----------------accept user inputs------------------#
# # user_name = input('what is your name?: ') #this is string
# # print('Hello '+user_name)

# # user_age = int(input('how old are you?: ')) #cast them to int() or float() to use them as integers/floats
# # user_age += 1
# # print("you are "+str(user_age)+" years old")

# # user_height = float(input('how tall are you?: '))
# # print('you are '+str(user_height)+'cm tall.')


# #----------useful functions related to numbers------------#
# from ast import Lambda
# from audioop import reverse
# from calendar import EPOCH
# import math
# from os import utime
# pi = 3.14
# x = 1
# y = 4
# z = 5
# print(round(pi))#rounding
# print(math.ceil(pi))#roudning a number up --> using ceil()
# print(math.floor(pi))#rounding a number down --> using floor()
# print(abs(pi))#absolute value of number --> how far the number away from zero
# print(pow(pi,2))  #power --> raise a number to a given power number ex: pi * pi
# print(math.sqrt(pi)) #getting the square root of a number
# print(max(x,y,z))#max --> getting the largest value
# print(min(x,y,z))#max --> getting the smallest value


# #-----------strings slicing(useed to create a substring by extrcting elements from another string)--------------#
# #[start:stop:step]
# name_slice = "Nanduni Kaveesha"

# first_name_slice = name_slice[0:8] #stopping index's character won't print....step:1 by default
# print(first_name_slice)

# last_name_slice = name_slice[8:]#or [8:16]
# print(last_name_slice)

# funky_name_slice = name_slice[::2]
# print(funky_name_slice)

# reversed_name_slice = name_slice[::-1] #reversing a name
# print(reversed_name_slice)

# website_slice = "https://google.com"
# website_slice2 = "https://wikipedia.com"
# webSite_slice_1 = slice(8,-4) #can use negative and positive indexing combination
# print(website_slice[webSite_slice_1])
# print(website_slice2[webSite_slice_1])


# #-------------if/ifelse statements-----------------#
# # age = int(input('how old are you? '))

# # if age ==100:#comparison operator for equality is '=='
# #   print('you are a century old')
# # elif age < 0:
# #   print("you haven't born yet")
# # elif age >= 18:
# #   print('you are an adult')
# # else:
# #   print('you are a child')

# #---------logical operators(and,or,not)----------------#
# # temp = int(input('what is the temperature outside? '))

# #and -> to check if two or more conditions are true or false/checking certain range
# # if (temp >= 0 and temp <= 20):
# #   print('temperature is good today!!!, run away !!!')
# # if(temp < 0 or temp > 30):
# #   print('temperature is bad !!!, die inside !!!')

# #not -> flipped it to true -> false / false -> true


# #----------while loop(a statement that willexecute it's block of code as long as it's conditions remains true)----#
# # name_while = None
# # while not name_while:
#   # name_while = input('enter your name: ')

# # print('hello '+name_while)
  

# #---------forloops(a statement that will execute a block of code limited, defined amount of time)----------#

# # for i in range(10): #works 10times(0-9)
# #   print(i+1)

# # for i in range(50,100): #first number inclusive, second number desclusive (50-99)
# #   print(i)

# #   #(start,end,step)
# #   for i in range(50,100,2):
# #     print(i)

# #   for i in "Nanduni Kaveesha":
# #     print(i)


# #---------count down to 10 - 0 after that a message-----#
# # import time

# # for seconds in range(10,0,-1):
# #   print(seconds)
# #   time.sleep(1) #program waits for 1 second
# # print("happy new year !")


# #----------nested loops-> (one loop inside another loop)the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"-------#

# # rows_nested = int(input('how many rows? '))
# # columns_nested = int(input('how many columns? '))
# # symbol_nested = (input('enter a symbol to use? '))


# # for i in range(rows_nested):
# #   for j in range(columns_nested):
# #     print(symbol_nested, end="")
# #   print()


# #-----------loop control statements(change loop execution from its normal sequence)-------------#

# #break -> use to terminate the loop entirely
# # while True:
# #   name = input('enter your name: ')
# #   if name != "":
# #     break

# #continue -> skips to the next iteration of the loop
# # phone_number = "123-345-5656"
# # for i in phone_number:
# #   if i == "-":
# #     continue
# #   print(i, end="") #end="" -> to print all items in one line

# #pass -> does nothing, acts as a placeholder
# # for i in range(1,21):
# #   if i == 13:
# #     pass
# #   else:
# #     print(i)


# #-------------lists-->stores multiple items within a single variable------------------#

# food =['pizza','pineapple','burger','noodles','hotdog','spaghetti']
# print(food) #printing all the list
# print(food[0]) #getting a one specific number using it's index

# food[0] = 'sushi'#updating/changing a specific index's item

# for x in food:
#   print(x)


# #--------useful functions of list----------------#
# food.append('ice cream') #adding an item at the end of list
# food.remove('sushi') #removing an item
# food.pop() #removing the last element
# food.insert(0,'banana') #insert a value to an specific index
# food.sort() #sorting the list alphabetically
# food.clear() #removing all the elements of a list


# #-----------2D lists(mulideminetional list)-> a list of lists------------#
# drinks = ['coffee','soda','tea']
# dinner = ['pizza','burger','sushi']
# desserts = ['ice cream','cake']

# food = [drinks, dinner, desserts]#adding all list to one list
# print(food)
# print(food[0][0])  #accessing the first list's first element


# #---------tuples->(collection ordered and unchangeable used to group related data)-------------#
# student = ("nanduni",21,"female")
# print(student.count("nanduni")) #to get how many times an item appears
# student.index("female") #to find the index of a certain value

# for x in student:
#   print(x)

# if "nanduni" in student:
#   print("nanduni is here")


#   #-------------set->collection is unordered, unindexed, no duplicate values-----------#
#   #**set is faster than list to check an item's existence, and it doesn't allow duplication
# #   utensils = {"fork","spoon","knife"}
  
# # utensils.add("napkin") #adding items
# # utensils.remove("fork") #removing element
# # utensils.clear()#removing all items

# # dishes = {"bowl","plate","cup","knife"}
# # utensils.update(dishes) #dishes adding to utensils
# # dinner_table = utensils.union(dishes)

# # # print(dinner_table)

# # print(utensils.difference(dishes)) #print what utensils has that dishes doesnt

# # print(utensils.intersection(dishes)) #prints what they both have in common


# #---------dictionaries -> changeable, unordered, unque key:value pairs----------#
# capitals = {'USA':'Wahington DC','India':'New Delhi','China':'Beijin','Russia':'Moscow'}
# print(capitals['USA']) #printing the value of the mentioned key
# print(capitals.get('Germany')) #to check if specific key exists in a dictionary
# print(capitals.keys()) #to get only the keys
# print(capitals.values()) #to get only the values
# print(capitals.items()) #to get all items(keys and values)

# capitals.update({'Germany':'Berlin'}) #adding a new item
# capitals.update({'USA':'Las Vegas'}) #updating an existing item
# capitals.pop('China') #to remove key and value of mentioned item
# capitals.clear() #to remove all items of the dictionary

# for key, value in capitals.items():
#   print(key, value)


# #------------index operator [] = give access to sequence's element (str, list, tuples)-----------#

# name = "nanduni Kaveesha"

# # if(name[0].islower()):
# #   name = name.capitalize()

# #creating substrings
# first_name_subs = name[:7].upper()
# print(first_name_subs)

# last_name_subs = name[8:].lower()
# print(last_name_subs)

# last_character = name[-1]
# print(last_character)
# print(name)


# #---------------functions -> a block of code which is executed only when it is called-------#
# def hello(first_name, last_name, age): #declaring the function
#   print('Hello bitch! '+first_name+" "+last_name)
#   print('you are '+str(age)+'years old')

# hello("Nanduni","Kaveesha",21) #calling the function
# hello("dude","bro",12)

# name_func = "www"
# hello(name_func, name_func,23)


# #--------return statement->functions send python values/objects back to the caller. these values/objects are known as the function's return value--------------#
# def multiply(number1, number2):
#   return number1 *number2


# #------keyword arguments-->>arguments preceded by an identifier when we pass them to a function the order of the argument doesn't matter, unlike positional arguments python knows the names of the arguments that our functions receives------------#
# def hello_positional_arguments(first,second,last):
#   print('Hello '+first+" "+second+" "+last)

# hello_positional_arguments(last='Nanduni',second='Kaveesha',first='Senadeera')

# def hello_keyword_arguments(first1,second2,third3):
#   print('Hello '+first1+' '+second2+' '+third3)

# hello_keyword_arguments(first1='Nanduni',third3='Senadeera',second2='Kaveesha')


# #---------nested function calls-->function calls inside of another function calls--innermost function calls are resolved first returned value is used as argument for the nested outer function----------------#

# # num = input('enter a whole positive number: ')
# # num = float(num)
# # num = abs(num)
# # num = round(num)
# # print(num)

# # print(round(abs(float(input('Enter a whole positive number: ')))))


# #variable scope->the region that a variable recognized, only avaialable in the region created (global/local can be created too)-------#

# name_scope = 'bro' #global scope
# def display_name_scope():
#   name_scope='code' #local scope(only inside of the function)
#   print(name_scope)

# display_name_scope()
# print(name_scope) #can't access,out of created region


# #--------args parameter -->>a parameter that will pack all arguments into a tuple, usefil so that a function can accept a varying amount of arguments-------#
# def add_args(*args): # '*'is important it does tha packing as the tuple 'args' name is changeable
#   sum = 0
#   stuff = list(args) #casting to a list
#   stuff[0]=0 #tuples can't be updated that's why it cast into a list
#   for i in stuff:
#     sum +=i
#   return sum

# print(add_args(1,2,3,4,5))


# #------kwargs(keyword arguments)-->>a parameter that will pack all arguments into a dictionary---------------#

# def hello_kwargs(**kwargs): #'**' is essential, it declares a dictionary
#   print("Hello ", end="")  #dictionary name['key name']
#   for key,value in kwargs.items():
#     print(value, end=" ")
#   print()

# hello_kwargs(title="Mr.",first='Nanduni',last='Kaveesha',middle='Senadeera')


# #----------str.format() method-->>method available to string(optional), gives user more about the output------------#
# animal = 'cow'
# item = 'moon'
# # print('The '+animal+' jumped over the '+item)
# print('The {} jumped over the {}'.format(animal,item)) #positional arguments
# print('The {1} jumped over the {0}'.format(item,animal)) #positional arguments
# print('The {animal1} jumped over the {item1}'.format(animal1='cow',item1='moon')) #keyword arguments

# text_format = 'The {} jumped over the {}'
# print(text_format.format(animal,item))

# name_format = 'Nanduni'
# print('Hello my name is {}'.format(name_format))
# print('Hello my name is {:10}. nice to meet you'.format(name_format)) #':10'-->> no of spaces after the name displayed
# print('Hello my name is {:<10}. nice to meet you'.format(name_format))#to add spaces after name
# print('Hello my name is {:>10}. nice to meet you'.format(name_format))#to add spaces before name

# number_format = 1.2344
# print('the number pi is {:.2f}'.format(number_format)) #2f-->>to display only first two digits after the decimal(f -> floats)

# number_format2 = 1000
# print('the number is {:,}'.format(number_format2))#adding ',' after the first digit
# print('the number in binary is {:b}'.format(number_format2))#to get the binary representation of the number
# print('the number in octal is {:o}'.format(number_format2))#to get the octal representation of the number
# print('the number in hexadicimal is {:x}'.format(number_format2))#to get the hexadecimal representation of the number
# print('the number in scientific notation is {:e}'.format(number_format2))#to get the scientific notation representation of the number


# #-----------methods using 'random'-------------#
# import random

# x_random = random.randint(1,6) #to get a number between 1 and 6
# print(x_random)

# y_random = random.random() #to get a floating number
# print(y_random)

# myList_random = ['rock','paper','scissor']
# z_random = random.choice(myList_random) #to get a random item from a list
# print(z_random)

# cards_random = [1,2,3,4,5,6,7,8,9,'J','K','Q']
# random.shuffle(cards_random) #to shuffle a list or other collection
# print(cards_random)


# #------------------exception handling--------------------#
# #---exception-->>is an event detected during execution which  interrupt the flow of the program-----------#
# # try:
# #     numerator_exception = int(input('enter a number to divide: '))
# #     denominator_exception = int(input('enter a number to divide by: '))
# #     result_exception = numerator_exception/denominator_exception
# # #first catch specific exceptions, then catch the normal exception
# # except ZeroDivisionError as e: #'as e'-->>to print the exception that displays by the python(optional)
# #   print(e)
# #   print("you can't divide by zero, idiot")
# # except ValueError as e:
# #   print(e)
# #   print("Enter only numbers please asshole")
# # except Exception as e:
# #   print(e)
# #   print('something went wrong')
# # else: #optional
# #   print(result_exception)
# # finally:#with or without exception always, finally block gets executed ex:to close files which are opened
# #   print('this will always execute !!!')


# #-------------basic file detections--------------------#
# # import os

# # path ="D:\\Program Files\\python full course\\python-full-course\\text.txt" #if you have backslash '\' in file path, use '\\' double backslash(that's the escape sequence for a backslash string)
# # if os.path.exists(path): #---checking file's existence---#
# #   print('that location exist !!!')
# #   if os.path.isfile(path): #---checking if it's a file--#
# #     print('this is a file')
# #   elif os.path.isdir(path): #---checking if it's a folder--#
# #     print('this is a directory')
# # else:
# #   print('that location doesnt exist !!!')


# # #------------------reading a file----------------------#
# # try:
# #     with open('text2.txt') as file: #this closes file automatically

# #     #doesnt need if files on project folder or else input the path ex'D:\\Program Files\\python full course\\python-full-course\\text.txt'
# #       print(file.read())
# # except FileNotFoundError:
# #   print('file was not found') 
# # print(file.closed) #to check if file is closed


# # #---------------writing files-------------------------#
# # text_write = 'yoooooooooooo\nThis is some text\nHave a good one:\n' #'\n'-->>causing a new line
# # with open('text-writing.txt','w') as file_writing:
# #    file_writing.write(text_write)

# # #----to append some text----#
# # text_write2 = 'have a nice day! see ya(appending text)'
# # with open('text-writing.txt','a') as file_writing:
# #   file_writing.write(text_write2)


# # #-------------copying files---------------------------#
# # import shutil
# # #3 ways
# # #1.copyfile() = copies contents of a file
# # #2.copy() = copyfile() + permission mode + detimation can be a directory
# # #3.copy2() = copy() + copies metadata (file's creation and modification times)

# # shutil.copyfile('text2.txt','copy.txt') #(src, destination) #if its not on project directory, name the location--------'copy.text' creating automatically

# # #copy() and copy2() are same


# # #--------------move files/folders-------------------------------#
# # import os
# # source_move = "move.txt" #if some place else give the path
# # destination_move = "D:\\Program Files\\moved.txt" #can rename the file's name

# # try:
# #   if os.path.exists(destination_move):
# #     print('theres already a file there')
# #   else:
# #     os.replace(source_move,destination_move) #moving the file
# #     print(source_move+ ' was moved')
# # except FileNotFoundError:
# #   print(source_move+' was not found')


# #-------------delete files----------------------#
# import os

# path='delete file.txt'

# #exception handling is exceptional
# try:
#   os.remove(path) #insert the file path if it's not in project repository
# except FileNotFoundError:
#   print('That file was not found')

# #--os.remove() function does not remove empty folders
# path_delete = 'empty delete folder'
# try:
#   os.remove(path_delete)

#   #to remove empty folders
#   os.rmdir(path_delete)
# except PermissionError:
#   print('you do not have permission to delete that')
# else:
#   print(path_delete+' folder is deleted')

# #--os.rmdir() function does not delete not empty folders
# path_folder_delete = 'not empty folder'

# try:
#   os.rmdir(path_folder_delete)
# except OSError:
#   print('you cannot delete that using that function')

# #shutil.rmtree() ->to delete not empty folders
# import shutil
# try:
#   shutil.rmtree(path_folder_delete) #this will delete the folder including all the includes
# except OSError:
#   print('you cannot delete that using that function')
# else:
#   print('folder is deleted')


#   #----------modules-->>a file containing python code, may contain functions, classes, etc. used with modular programming, which is to seperate a program into parts.--#
# import messaages_modules as msg #module file name

# #-----another way to import modules----#
# # from messaages_modules import hello_modules, bye_modules
# # from messaages_modules import * #to import all function

# msg.hello_modules()#using a function from that imported module
# msg.bye_modules()

# #to populate all the modules that available for the file
# # help('modules')


# #----------basic game--->>rock, paper, scissor--------#
# # import random

# # while(True):
# #   choice_rps = ['rock','paper','scissor']
# #   computer_rps_choice = random.choice(choice_rps)

# #   player_rps_choice = None

# #   while player_rps_choice not in choice_rps:
# #     player_rps_choice = input('rock, paper or scissor?: ').lower()

# #   if player_rps_choice == computer_rps_choice:
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('Tie !!!')
# #   elif player_rps_choice == 'rock':
# #     if computer_rps_choice == 'paper':
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('you lose !!!')
# #     if computer_rps_choice == 'scissor':
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('you win !!!')
# #   elif player_rps_choice == 'scissor':
# #     if computer_rps_choice == 'paper':
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('you win !!!')
# #     if computer_rps_choice == 'rock':
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('you lose !!!')
# #   elif player_rps_choice == 'paper':
# #     if computer_rps_choice == 'rock':
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('you win !!!')
# #     if computer_rps_choice == 'scissor':
# #       print('computer : ',computer_rps_choice)
# #       print('player : ',player_rps_choice)
# #       print('you lose !!!')
  
# #   play_again = input('play again(yes/no): ')
# #   if play_again != 'yes':
# #     break
# # print('Bye !')


# #------------check basic quiz game.py------------------#
# #-----------check poop.py for (python object oriented programming)-------------#
# from poop import Car

# #in python we do not have to pass 'self' that automatically has done for us
# car_1 = Car('Chevy','Corvette',2021,'Blue')
# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)
# car_1.drive()
# car_1.stop()

# car_2 = Car('ford','mmustang',2022,'red')
# car_2.drive()
# car_2.stop()
# #class-->> can function as a blue print to create objects, we can assing attributes, methods, innit method's arguments can pass in when creating an object


# #------------basics of class variables-------------------#
# #-----difference between class variables and instance variables----#
# car_1_class = Car('Chevy','Corvette',2021,'Blue')
# car_2_class= Car('ford','mmustang',2022,'red')

# car_1_class.wheels = 2 #accessing class variables using it's object

# Car.wheels =2 #accessing class variables using class

# print(car_1_class.wheels)
# print(car_2_class.wheels)


# #-------------------inheritence------------------------#
# #---means classes can have childrens and it  gives all(attributes,methods) parents have to children---#
# #----each child classes have thier own things(attributes,methods) too---#
# #----------check animals.py for more-----------#


# #-----------multilevel inheritence =>> when a derived(child) class inherits another derived(child) class------#

# #----like a family tree-->>inhert from grand parents to parents to childrens----#
# class Organism:
#   alive = True

# class Animal(Organism):
#   def eat(self):
#     print('this animal is eating')

# class Dog(Animal):
#   def bark(self):
#     print('this dog is barking')

# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()


# #------------------mutiple inheritence-->>when a child class is derived from more than one parent class------#

# #-----as an example some animals can be a prey or predator differs from situation to situation------#
# class Prey:
#   def flee(self):
#     print('this animal flees')

# class Predator:
#   def hunt(self):
#     print('this animal is hunting')

# class Rabbit(Prey):
#   pass
# class Hawk(Predator):
#   pass
# class Fish(Prey,Predator):
#   pass

# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()

# #fishes can be flee and hunt
# fish.flee()
# fish.hunt()


# #----------method oerriding-->>child clss hs specific ability to get a specific implimentation of already defined method in parent's class-------------------------#
# class Animal_oerride:
#   def eat(self):
#     print('This animal is eating')

# class Rabbit_override(Animal):
#   def eat(self):
#     print('This rabbit is eating a carrot')

# rabbit_override = Rabbit_override()
# rabbit_override.eat() #this will implement the most close method


# #--------method chaining-->>calling multiple methods sequentially each call performs an action on the same object and returns self---------------#
# class Car_chaining:
#   def turn_on_chaining(self):
#     print('you start the engine')
#     return self
  
#   def drive_chaining(self):
#     print('you drive the car')
#     return self

#   def brake_chaining(self):
#     print('you stepped on the brake')
#     return self

#   def turn_off_chaining(self):
#     print('you turned off the engine')
#     return self

# car_chaining = Car_chaining()

# car_chaining.turn_on_chaining()
# car_chaining.drive_chaining()

# #----method chaining using----#
# #****to use method chaining we have to 'return self' after each method--->>>because it'll return self then that object will call the next one
# car_chaining.turn_on_chaining().drive_chaining()

# #--------when having multiple methods callings in method chaining-----#
# car_chaining.turn_on_chaining()\
#             .drive_chaining()\
#             .brake_chaining()\
#             .turn_off_chaining()


# #-----------super()-->>used to give access to the methods of a parent class. returns a temperory object of a parent class when used-------#
# class Rectangle_super:
#   def __init__(self,length,width):
#     self.length = length
#     self.width = width

# class Square_super(Rectangle_super):

#   def __init__(self,length,width):
#     super().__init__(length,width)

#   def area(self):
#     return self.length * self.width


# class Cube_super(Rectangle_super):

#   def __init__(self, length, width, height):
#     super().__init__(length,width)
#     self.height = height
  
#   def volume(self):
#     return self.length * self.width * self.height

# square_super = Square_super(3,3)
# cube_super = Cube_super(2,3,4)

# print(square_super.area())
# print(cube_super.volume())


# #------------------abstract classes-->>prevent the user from creating an object of the class, comples a user to override abtract methods in a child class---#
# #abstract class-->> a class which contain one or more abstrsct methods---#
# #abstract methods-->> a method that has a declaration but does not have an implementation---#

# #abc-->>abstract based class
# from abc import ABC, abstractmethod 
# #to make it abstract-->> import this first

# class Vehicle_abstract(ABC):

#   @abstractmethod #to make it abstract metod
#   def go(self):
#     pass

#   @abstractmethod
#   def stop(self):
#     pass
#   #child classes always should implement pabstract class's all methods

# class Car_abstract(Vehicle_abstract):
#   def go(self): #overriding the method
#     print('you drive the car')

#   def stop(self):
#     print('this car is stopped')

# class MotorCycle_abstract(Vehicle_abstract):
#   def go(self):
#     print('you ride the motorcycle')

#   def stop(self):
#     print('this motorcycle is stopped')

# # vehicle_abstract = Vehicle_abstract() #cant do this cant make childs from abstract classes
# car_abstract = Car_abstract()
# motorCycle_abstract = MotorCycle_abstract()

# car_abstract.go()
# car_abstract.stop()

# motorCycle_abstract.go()
# motorCycle_abstract.stop()


# #-------------------pass objects as arguments--->>

# class Car_passObjects:
#   color = None

# class MotorCycle_passObjects:
#   color = None

# def change_color_objects(vehicle,color):
#   vehicle.color = color
  
# car_1_object = Car_passObjects()
# car_2_object = Car_passObjects()
# car_3_object = Car_passObjects()

# change_color_objects(car_1_object,"blue")
# change_color_objects(car_2_object,"red")
# change_color_objects(car_3_object,"yellow")

# print(car_1_object.color)
# print(car_2_object.color)
# print(car_3_object.color)

# bike_1_object = MotorCycle_passObjects()
# change_color_objects(bike_1_object,'black')
# print(bike_1_object.color)


# #----------duck typing--->>concept where the class of an object is less important than the methods/attributes. class type is not checked if minimum methods/attributes are present, 'if it walks like a duck and it quacks like a duck, then it must be a duck'
# class Duck:
#   def walk(self):
#     print('this duck is walking')

#   def talk(self):
#     print('this duck is qwuacking')

# class Chicken:
#   def walk(self):
#     print('This chicken is walking')
    
#   def talk(self):
#     print('This chicken is clucking')

# class Person:

#   def catch(self,duck):
#     duck.walk()
#     duck.talk()
#     print('you caught the critter!')

# duck = Duck()
# chicken = Chicken()
# person = Person()

# #since chicken has methods walk and talk it works here too
# person.catch(chicken)


# #----------walrus operator(:=)--->>1.assingment expression aka walrus operator, 2.assgins values to varaibles as part of a larger expression----#

# # happy = True
# # print(happy)
# #to do that in oneline...........
# print(happy := True)

# # foods = list()
# # while True:
# #   food = input('what food do u like?: ')
# #   if food == 'quit':
# #     break
# #   foods.append(food)
# #this using walrus operator..............

# # foods = list()
# # while food := input('what food do you like?: ') != 'quit':
# #   foods.append(food)


# #-------how to assign function to a variable---------#
# # def hello_function():
# #   print('hello')

# # print(hello_function) #this will print the memory address of the function
# # hi_function = hello_function  #after this we can use 'hi_function' variable as the 'hello' function
# # print(hi_function())
# # print(hello_function())

# say = print #assiging print() function to 'say' variable
# say('whoa : I cant believe this works')


# #higher order functions--->>>these functions,1. accepts function as an argument or 2. returns a function

# #---1.higher order function->accepts function as an argument--
# def loud(text):
#   return text.upper()

# def quiet(text):
#   return text.lower()

# def hello(func):
#   text = func('hellow')
#   print(text)

# hello(loud) #passing loud function as loud variable using function using as a variable
# hello(quiet)

# #--higher order function->2.returns a function--#
# def divisor(x):
#   def dividend(y):
#     return y/x
#   return dividend   #this return the function

# divide = divisor(2)
# print(divide(10))


# #-------lambda function-->>function written in oneline using lamda keyword accepts any number of argument, but only has one expression.(think of it as a shortcut),  useful if needed for a short period of time(can only use once), throw-away.

# #this is how it works
# #lamda parameter:expression

# # def double(z):
# #   return z *2
# # print(double(2))
# #to make it lamda function...........

# double = lambda x:x * 2
# print(double(5))

# multiply = lambda x,y:x*y
# print(multiply(1,4))

# add = lambda x,y,z:x+y+z
# print(add(3,5,6))

# fullname = lambda first_name,last_name:first_name+" "+last_name
# print(fullname('nanduni','kaveesha'))

# #--if else with lambda
# age_check = lambda age:True if age >= 18 else False
# print(age_check(12))


# #-----------sort() method = used with lists-----------#
# students = ['squidward','spongebob','patrick','sandy','krabs'] 

# #only lists can use sort()
# students.sort() #sorting alphabetical order
# for i in students:
#   print(i)

# students.sort(reverse=True) #to print it in reverse order
# for i in students:
#   print(i)

# #----sort() function = used with iterables-----#
# students_tuple = ('squidward','spongebob','patrick','sandy','krabs')
# sorted_students = sorted(students_tuple) #ths will return a lists but accepts iterables
# for i in sorted_students:
#   print(i)

# sorted_students_reverse = sorted(students_tuple,reverse=True) #ths will return a lists but accepts iterables
# for i in sorted_students_reverse:
#   print(i)

# #list of tuples
# student_listtuple = [('squidward','F',60),
#                     ('sandy','A',33),
#                     ('patrick','D',36),
#                     ('spongebob','B',20),
#                     ('Krabs','C',78)]

# student_listtuple.sort()#to sort by first column
# for i in student_listtuple:
#   print(i)
 
# grade = lambda grades:grades[1]
# student_listtuple.sort(key=grade)#to sort by first column
# for i in student_listtuple:
#   print(i)

# #tuple of tuples
# student_tupletuple = (('squidward','F',60),
#                     ('sandy','A',33),
#                     ('patrick','D',36),
#                     ('spongebob','B',20),
#                     ('Krabs','C',78))

# age = lambda ages:ages[2]
# sorted_student_tupletuple = sorted(student_tupletuple,key=age)
# for i in sorted_student_tupletuple:
#   print(i)


# #-----------------map()--->>applies a function to each in an iterable(list, tuple, etc.)

# #map(function,iterable)
# #list of tuples
# store = [('shirt',20.00),
#         ('pants',25.00),
#         ('jacket',50.00),
#         ('socks',10.00)]
# to_euros = lambda data : (data[0],data[1]*0.82)

# store_euros = list(map(to_euros,store))
# for i in store_euros:
#   print(i)


# #--------------filter()-->>creates a collection of elements from an iterable for which a function returns true.

# #filter(function,iterable)
# friends = [('rachel',19),
#           ('monica',18),
#           ('phoebe',17),
#           ('joey',16),
#           ('chandler',21),
#           ('ross',20)]

# age_filter = lambda data:data[1] >= 18
# drinking_boddies = list(filter(age_filter,friends))
# for i in drinking_boddies:
#   print(i)


#   #-----------reduce()-->>apply a function to an iterable and reduce it to a single cumulative value. performs function on first two elements and repeats process until 1 value remains.------#
#   #reduce(function,iterable)
#   import functools
#   # letters_reduce= ['h','e','l','l','o']
#   # word_reduce = functools.reduce(lambda x,y,:x+y,letters_reduce)
#   # print(word_reduce)
#   factorial = [5,4,3,2,1]
#   result_factorial = functools.reduce(lambda x,y,:x*y,factorial)
#   print(result_factorial)


# #---list comprehension-->>a way to create a new list with less syntax, can mimic certain lambda functions, easier to read, ---list =[expression for item in iterable]-----#
#   squares_comprehension = []
#   for i in range(1,11):
#     squares_comprehension.append(i * i)

# #using list comprehension..........
# squares_list_comprehension = [i * i for i in range(1,11)]
# print(squares_list_comprehension)

# students_marks = [100,89,67,56,54,79]

# passed_students = list(filter(lambda x:x>= 60, students_marks))
# print(passed_students)

# #using list comprehension.........
# #list =[expression for item in iterable if conditions]
# passed_students_comprehension = [i for i in students_marks if i >= 60]
# print(passed_students_comprehension)

# #using (if/else) list comprehension...........
# #list = [expression (if/else) for item in iterable]
# passsed_students_list_comprehension = [i if i>= 60 else "Faild" for i in students_marks]
# print(passed_students_comprehension)


# #---dictionary comprehension-->>create dictionaries using an expression, can replace fo loops and certain lambda functions
# #dictionary = {key:'expression' for (key,value) in 'iterable'};
# cities_in_F = {'New York':32,'Boston':75,'Los Angeles':100,'Chicago':50}
# cities_in_C={key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)

# #dictionary = {key:'expression' for (key,value) in 'iterable' if conditional};
# cities_in_weather = {'New York':'snowing','Boston':'sunny','Los Angeles':'sunny','Chicago':'cloudy'}
# #since doesnt have a function. 'function'-->>'key'
# sunny_weather = {key:value for (key,value) in cities_in_weather.items() if value == 'sunny'}
# print(sunny_weather)

# #dictionary = {key: (if/else) for (key,value) in iterable}
# desc_cities_in_weather = {key:("WARM" if value >= 40 else "COLD") for (key,value) in cities_in_C.items()}
# print(desc_cities_in_weather)

# #dictionary = {key:function(value) for (key,value) in iterable}
# def check_temp(value):
#   if value >= 70:
#     return "HOT"
#   elif 69 >= value >= 40:
#     return "WARM"
#   else:
#     return "'COLD"

# desc_cities_in_weather2= {key:check_temp(value) for (key,value) in cities_in_C.items()}
# print(desc_cities_in_weather2)


# #-----zip(*iterable)-->>aggregate elements from two ro more iterables(lists,tuples,sets,etc), create a zip object with paired elements stored in tuples for each element
# usernames = ['dude','nan','kaveesha']
# passwords = ('adadsa','344$fsdf','ervr@ef')

# users_zip =list(zip(usernames,passwords))#now we have list of tuples
# users_zip_dic = dict(zip(usernames,passwords))

# print(type(users_zip))
# for i in users_zip:
#   print(i)

# for key,value in users_zip_dic.items():
#   print(key+" : "+value)

# login_dates = ['1/1/2022','1/2/2022','1/3/2022']
# users_pass_login = zip(usernames,passwords,login_dates)
# for i in users_pass_login:
#   print(i)


# #-----------if __name__ == '__main__'-------------#
# #why?
# #1.module can be run as a standalone program
# #2.module can be imported and used by other modules

# #pythno intrepeter sets "special variables", one of which is __name__
# #then python will execute the code found within __main__
# import module_two
# print(module_two.__name__)

# print(__name__)

# if __name__ =='__main__':
#   print('running this module directly')
# else:
#   print('running other module indirectly')

# #thiss cant run as standalone
# def using__name__():
#   print('Hello')

# #using __name__to run it
# if __name__=='__main__':
#   using__name__()

#   #-------times and date------------------#
# import time

# #epoch-->>a date and time from hich a computer measures system time
# print(time.ctime(0)) #ctime()-->converting a time expressed in seconds since epoch to a readable string

# print(time.ctime(1000000)) #1 million seconds

# #time method-->returns current seconds since epoch
# print(time.time())

# print(time.ctime(time.time()))

# time_object = time.localtime() #this is creating an object
# print(time_object)
# #strftime()-->>converting it to readable object
# local_time_readable = time.strftime("%B %D %Y %H:%M:%S",time_object)
# print(local_time_readable)

# #universal time
# time_object_uni = time.gmtime()
# print(time_object_uni)

# #strptime()-->>string time and date and return an object
# time_String = "20 April 2022"
# time_object_str= time.strptime(time_String,"%d %B %Y")
# print(time_object_str)

# #tuple representantion of time
# time_tuple=(2022, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string_asc = time.asctime(time_tuple)
# print(time_string_asc)

# #mktime()-->>take the time and convert it to seconds since epoch
# time_mk = time.mktime(time_tuple)
# print(time_mk)


#---------------------threading-----------------------#
#thread=a flow of an execution, like a seperate order of instructions, however each thread takes a turn to achieve concurrency GLI = (Global Interpreter Lock), allows only one thread to hold the control of the python interpreter

#cpu bound = program/task spends mot of it's time waiting for internal events(CPU interpreter) use multiprocessing

#io bound = program.task spends most of it's tme waiting for external events(user interpreter) use multithreading

# import threading
# import time
# print(threading.active_count())
# print(threading.enumerate())

# #these all are 'io bound'
# def eat_breakfast():
#     time.sleep(3) #the time taking for that
#     print('you eat breakfast')

# def drink_coffee():
#   time.sleep(4)
#   print('you drank coffee')

# def study():
#   time.sleep(5)
#   print('you finished studying')

# # #these all works after one another
# # eat_breakfast()
# # drink_coffee()
# # study()

# #but we humans can do all those tasks at once-->>multithreading(only taking-->>5secs)
# x = threading.Thread(target=eat_breakfast,args=()) #can add arguments too using-->>'args=()'
# x.start()

# y = threading.Thread(target=drink_coffee,args=()) #can add arguments too using-->>'args=()'
# y.start()

# z = threading.Thread(target=study,args=()) #can add arguments too using-->>'args=()'
# z.start()

# #to get how long it takes to complete the main thread
# print(time.perf_counter())

# #--------------thread synchronization-------------#
# x.join() #main threade has to wait to thread x to finish
# y.join()
# z.join()


#--------------daemon thread-->>a thread that runs in the background, not important for program to run, your program will not wait for daemon threads to complete before exiting, non-daemon threads cannot normally be killed, stay aline until task is complete-----------#

# #ex: background tasks, garbage collection, wating for input, long runnign precess
# import threading 
# import time

# def timer():
#   print()
#   count = 0
#   while True:
#     time.sleep(1)
#     count += 1
#     print('logged in for: ',count,' seconds')

# # x= threading.Thread(target=timer)
# # x.start()

# #changing x to daemon.....
# y=threading.Thread(target=timer, daemon=True)
# y.start()
# answer = input('Do you wish to exit?')


#-----------------multiprocessing-->>running tasks in parallel on different cpu cores, bypasses GIL used for threading
#multiprocessing = better for cpu bound tasks(heavy cpu usage)
#multithreading = better for io bound tasks (waiting around)

# from multiprocessing import Process, cpu_count
# import time

# def counter(num):
#   count = 0
#   while count < num:
#     count += 1

# def main():
#   a = Process(target=counter,args=(2500000000,))
#   b = Process(target=counter,args=(2500000000,))
#   c = Process(target=counter,args=(2500000000,))
#   d = Process(target=counter,args=(2500000000,))


#   a.start()
#   b.start()
#   c.start()
#   d.start()

#   a.join()
#   b.join()
#   c.join()
#   d.join()
  
#   print('finish in :',time.perf_counter()," seconds")
# if __name__=='__main__':
#    main()


#-----------GUI(Graphical User Interface)------------#
from cgitb import text
from email.mime import image
from tkinter import *
import tkinter
#widgets-->>GUI elements : buttons, textboxes, labels, images
#windows-->>serves as a container to hold or contain these widgets

# first_window_creation = Tk()#instantiate an instance of a window
# first_window_creation.geometry("420x420")
# first_window_creation.title("First GUI python")

# icon = PhotoImage(file='images/logo.png') #converting images to readable of python (only works for 'png')
# first_window_creation.iconphoto(True, icon)

# #to make changes to window can use 'config'
# first_window_creation.config(background='#5cfcff')#hexvalues works

# first_window_creation = mainloop() #place window on computer screen, listen for events


#--------label in python-->>an area widget that holds and/or an image within a window----#
# label_window = Tk()

# #'()' acts like arguments,'text' is a keyword arguments, creating the label

# #creating a photo for the label
# photo = PhotoImage(file='images/logo.png')

# first_label = Label(label_window,
#                     text='Hello World !!!',
#                     font=('Arial',40,'bold'),
#                     fg='#00FF00', #**fg(foreground-->>font color)
#                     bg='black', #bg(background color)
#                     relief=RAISED, #border styling adding
#                     bd=10,  #border width
#                     padx=20,#padding between x(text and border)
#                     pady=20,#padding between y(text and border)
#                     image=photo, #adding the photo to the label(only photo will show in window)
#                     compound='bottom'#to add photo and texts both to window(set in photo's location)
#                     ) 

# first_label.pack() #adding the created label to window

# # #another way to add the label....
# # first_label.place(x=100,y=100)

# label_window.mainloop()


#-----buttons--->>you click it, then it does stuff-----#
# count = 0
# def click_btn():
#   print('you clicked the button')
#   global count #to count how many times user clicked the button
#   count += 1
#   print(count)

# btn_window = Tk()

# photo=PhotoImage(file='images/logo.png')

# first_button = Button(btn_window, #creating the button
#                       text='click me',
#                       command=click_btn, #callback to a function
#                       font=('Comic-Sans',30),
#                       fg='#00FF00',#foreground=font color
#                       bg='black',
#                       activeforeground='#00FF00',
#                       activebackground='black', #set the active background color and background color to same to stop flashing the color
#                       state=DISABLED, #to stop user clicking enable
#                       image=photo, #will only show the image
#                       compound='bottom'#to driect the images place
#                       )

# first_button.pack()
# btn_window.mainloop()


#--------------entry box-->>textbox that accepts a simgle line of user input--------------------#
# def submit():
#   username = entrybox.get() #will return a string of the entry box
#   print('Hello '+ username)
#   entrybox.config(state=DISABLED) #to disable the entry box after entering text

# def delete():
#   entrybox.delete(0,END) #(firstcharqcter, lastcharacter)

# def backspace():
#   entrybox.delete(len(entrybox.get())-1 ,END)

# entrybox_window=Tk()

# entrybox = Entry(entrybox_window,
#                  font=('Arial',50),
#                  fg = '#00FF00',
#                  bg='black',
#                  show="x" #for get passwords
#                  )

# entrybox.insert(0,'spongebob') #default text to entry box
# entrybox.pack(side=LEFT)

# submit_btn = Button(entrybox_window,text='submit',command=submit)
# submit_btn.pack(side=RIGHT)

# delete_btn = Button(entrybox_window,text='delete',command=delete)
# delete_btn.pack(side=RIGHT)

# backspace_btn = Button(entrybox_window,text='backspace',command=backspace)
# backspace_btn.pack(side=RIGHT)

# entrybox_window.mainloop()


#-------------------checkbuttons------------------------#
# from tkinter import *
# def display():
#   if(x.get()==1):
#     print('you agree')
#   else:
#     print('you disagree :(')

# checkbutton_window = Tk()

# photo = PhotoImage(file='images/logo.png')

# x = IntVar() #to store int (normally stored 1 or 0)
# checkbtn_first = Checkbutton(checkbutton_window,
#                              text='i agree to something',
#                              variable=x,
#                              onvalue=1, #what would be stored in variable if user ticked the checkbox
#                              offvalue=0,  #what would be stored in variable if user didnt tick the checkbox
#                              command=display,
#                              font=('Arial',20),
#                              fg='#00FF00',
#                              bg='black',
#                              activeforeground='#00FF00',
#                              activebackground='black',
#                              padx=25,
#                              pady=10,
#                              image=photo,
#                              compound='left'
#                              )
# checkbtn_first.pack()                           
# checkbutton_window.mainloop()


#--------------------radiobuttons-----------------------#
# foodlist = ['pizza','hamburger','hotdog']

# def order():
#   if(x.get()==0):
#     print('you ordered pizza')
#   elif(x.get()==1):
#     print('you ordered hamburger')
#   elif(x.get()==2):
#     print('you ordered hotdog')
#   else:
#     print('huh !!!')



# radiobtn_window = Tk()

# Pizzaphoto = PhotoImage(file='images/logo.png')
# Hamburgerphoto = PhotoImage(file='images/logo.png')
# Hotdogphoto = PhotoImage(file='images/logo.png')

# foodImages=[Pizzaphoto,Hamburgerphoto,Hotdogphoto]

# x = IntVar()

# for index in range(len(foodlist)):
#   radiobtn_first = Radiobutton(radiobtn_window,          
#                               text=foodlist[index],
#                               variable=x, #group radiobuttons togather if they share..
#                               value=index, #set in value for radio buttons
#                               padx=25,
#                               font=('Impact',50),
#                               image=foodImages[index],
#                               compound='left',
#                               indicatoron=0, #eliminate circle indicators
#                               width=375, #sets width of radio buttons
#                               command=order
#                               )

#   radiobtn_first.pack(anchor=W) #to make in line up


# radiobtn_window.mainloop()


#-----------------------scale---------------------------#
# from tkinter import *

# def scale_submit():
#   print('temperature is: '+str(first_scale.get())+' degrees C.')
# scale_window = Tk()

# hotphoto = PhotoImage(file='images/logo.png')
# hotLabel = Label(image=hotphoto)
# hotLabel.pack()

# first_scale = Scale(scale_window, 
#                     from_=0,
#                     to=100,
#                     length=600, #hieght of the scale
#                     orient = VERTICAL, #orientation of scale
#                     font=('Consolas',20),
#                     tickinterval=10, #show the numeric indicator from 10 to 10
#                     # showvalue=0,#hide current value
#                     resolution = 5, #increment of slider
#                     troughcolor='#69EAFF',
#                     fg='#FF1C00',
#                     bg='black'
#                     )
# first_scale.set(50) #chang ethe indicator's position to 100

# #to make the indicator middle always
# first_scale.set((first_scale['from']-first_scale['to'])/2+first_scale['to'])

# first_scale.pack()


# coldphoto = PhotoImage(file='images/logo.png')
# coldLabel = Label(image=coldphoto)
# coldLabel.pack()

# scale_btn = Button(scale_window,text='submit',command=scale_submit)
# scale_btn.pack()

# scale_window.mainloop()


#---------------list box -->> A listing of seelectable text items within it's own container-----------------#
# def listbox_submit():
#   food = []
#   for index in first_listbox.curselection():
#     food.insert(index,first_listbox.get(index))

#   print('you have ordered : ')
#   for index in food:
#     print(index)
#   # print(first_listbox.get(first_listbox.curselection())) #to get the current selected item


# def listbox_add():
#   first_listbox.insert(first_listbox.size(),listbox_entrybox.get())
#   first_listbox.config(height=first_listbox.size())#to adjust the size of list box accordingly

# def listbox_delete():
#   # first_listbox.delete(first_listbox.curselection())
#   for index in reversed(first_listbox.curselection()):
#     first_listbox.delete(index)
#   first_listbox.config(height=first_listbox.size())#to adjust the size of list box accordingly

# from tkinter import *

# listbox_window = Tk()

# first_listbox = Listbox(listbox_window,
#                        bg='#f7ffde',
#                        font=('Constantia',35),
#                        width=12,
#                        selectmode=MULTIPLE #to make listbox select more than one item
#                        )
# first_listbox.pack()

# first_listbox.insert(1,'pizza')
# first_listbox.insert(2,'pasta')
# first_listbox.insert(3,'garlic bread')
# first_listbox.insert(4,'soup')
# first_listbox.insert(5,'salad')

# first_listbox.config(height=first_listbox.size())#to adjust the size of list box accordingly

# listbox_entrybox = Entry(listbox_window)
# listbox_entrybox.pack()

# listbox_submit_btn = Button(listbox_window, text='submit',command=listbox_submit)
# listbox_submit_btn.pack()

# listbox_add_btn = Button(listbox_window, text='add',command=listbox_add)
# listbox_add_btn.pack()

# listbox_delete_btn = Button(listbox_window, text='delete',command=listbox_delete)
# listbox_delete_btn.pack()


# listbox_window.mainloop()


#-------------------messageboxes-------------------------#
# from tkinter import *
# from tkinter import messagebox #import messagebox library

# def click():
  # messagebox.showinfo(title='this is n info message box',message='you are a person')
    # messagebox.showwarning(title='WARNING!',message='you have a virus')
    # messagebox.showerror(title='ERROR!',message='something went wrong')

    # if(messagebox.askokcancel(title='ask ok cancel', message='do you want to do the thing?')):
    #   print('you did a thing')
    # else:
    #   print('you canceled a thing')

    # if(messagebox.askretrycancel(title='ask retry cancel', message='do you want to retry the thing?')):
    #   print('you retry a thing')
    # else:
    #   print('you canceled a thing')

    # if(messagebox.askyesno(title='ask yes or no', message='do you like cake?')):
    #   print('i like cake too')
    # else:
    #   print('why do you not like cake')

    # answer = messagebox.askquestion(title='ask question', message='do you like pie?')
    # if(answer=='yes'):
    #   print('i like pie too')
    # else:
    #   print('why do you not like pie')

#    answer= messagebox.askyesnocancel(title='ask yes no cancel',message='do you like to code?',icon='warning') #icons ='info' or 'error'
#    if(answer==True):
#      print('you like to code')
#    elif(answer==False):
#       print('why are you watching a coding video??')
#    else:
#      print('you have dodged the question')

# msgbox_window = Tk()

# msgbox_btn = Button(msgbox_window,command=click,text='clickme')
# msgbox_btn.pack()

# msgbox_window.mainloop()


#--------------------colorchooser----------------------#
# from tkinter import *
# from tkinter import colorchooser #this is a submodule thats why
# def click_colorchooser():
#   # color = colorchooser.askcolor() #can pick a color after selecting button
#   # colorHex = color[1]
#   # print(colorHex)
#   # colorchooser_window.config(bg = colorHex) #this will change background color

#   #to get all the above done in oneline..........
#   colorchooser_window.config(bg = colorchooser.askcolor()[1])

# colorchooser_window = Tk()

# colorchooser_window.geometry('420x420')

# colorchooser_btn = Button(colorchooser_window,text='click me',command=click_colorchooser)
# colorchooser_btn.pack()

# colorchooser_window.mainloop()


# #--------------text widget-->> fucntions like a text area, you can enter multiple lines of text------------#
# from tkinter import *

# def textarea_submit():
#   input = text.get("1.0",END) #(starting index, ending index)
#   print(input)


# textarea_window = Tk()

# text = Text(textarea_window,
#             bg = 'light yellow',
#             font=('Ink Free',25),
#             height=8,
#             width=20,
#             padx=20,
#             pady=20,
#             fg='purple'
#            )
# text.pack()

# textarea_btn = Button(textarea_window,text='submit',command=textarea_submit)
# textarea_btn.pack()

# textarea_window.mainloop()


#------------file dialog to open and read a file-------#
# from tkinter import *
# from tkinter import filedialog

# def openFile():
#   # filepath = filedialog.askopenfilename() #getting the user selected folder file path
#   filepath = filedialog.askopenfilename(initialdir="D:\\Program Files\\python full course\\openFile_fileDialog\\openFile.txt",
#   title='Open File okay?',
#   filetypes=(('txt files','.txt'),
#             ("all files","*.*"))
#   )
#   file = open(filepath,'r') #'r' for reading
#   print(file.read())
#   file.close()

# fileDialog_openFile_window = Tk()

# openFile_btn = Button(fileDialog_openFile_window,text='open',command=openFile)
# openFile_btn.pack()

# fileDialog_openFile_window.mainloop()


#--------------saving a file using file dialog----------#
# from tkinter import *
# from tkinter import filedialog

# def saveFile():
#   file = filedialog.asksaveasfile(initialdir='D:\\Program Files\\python full course\\openFile_fileDialog',
#                                   defaultextension='.txt',
#                                   filetypes=[
#                                     ("Text file",".txt"),("HTML file",".html"),("All files","*.*"),]
#                                   )

#   if file is None:
#     return
#   # fileText = str(saveFile_text.get(1.0,END)) #has to convert into string to save
#   fileText = input('enter some texts please...')
#   file.write(fileText)
#   file.close()

# fileDialog_saveFile_window = Tk()

# saveFile_btn = Button(fileDialog_saveFile_window,text='save',command=saveFile)
# saveFile_btn.pack()
# saveFile_text = Text(fileDialog_saveFile_window)
# saveFile_text.pack()

# fileDialog_saveFile_window.mainloop()


#------------------menubar------------------------------#
# from tkinter import *

# def openFile():
#   print('file has been opened')

# def saveFile():
#   print('file has been saved')

# def cut():
#   print('you have cut some text')

# def copy():
#   print('you have coppied some text')

# def paste():
#   print('you have pasted some text')

# menubar_window = Tk()

# photo = PhotoImage(file='images/logo.png')

# first_menubar = Menu(menubar_window)
# menubar_window.config(menu=first_menubar)

# fileMenu = Menu(first_menubar,
#                 tearoff=0, #to get rid of the '------' line, in begining
#                 font=('MV Boli',15)
#               )
# first_menubar.add_cascade(label='File',menu=fileMenu) #this will have drop down menu effect
# fileMenu.add_command(label='Open',command=openFile,image=photo,compound='left') #a clickable option
# fileMenu.add_command(label='Save',command=saveFile) #a clickable option
# fileMenu.add_separator() #to add a separate line between 'save' and 'exit'
# fileMenu.add_command(label='Exit',command=quit) #quit-->>is a general command to exit

              
# editMenu = Menu(first_menubar,tearoff=0, font=('MV Boli',15))
# first_menubar.add_cascade(label='Edit',menu=editMenu)
# editMenu.add_command(label='Cut',command=cut) #a clickable option
# editMenu.add_command(label='Copy',command=copy) #a clickable option
# editMenu.add_command(label='Paste',command=paste) #a clickable option

# menubar_window.mainloop()


#---------------------frames-->> a rectangular container to group and hold widgets--------------------------#
# from tkinter import *
# frames_window = Tk()

# first_frame = Frame(frames_window,bg='pink',bd=5,relief=SUNKEN)
# first_frame.place(x=100,y=100) #replaced 'first_frame.pack()' with this


# Button(first_frame,text='W',font=('Consolas',25),width=3).pack(side=TOP)
# Button(first_frame,text='A',font=('Consolas',25),width=3).pack(side=LEFT)
# Button(first_frame,text='S',font=('Consolas',25),width=3).pack(side=LEFT)
# Button(first_frame,text='D',font=('Consolas',25),width=3).pack(side=LEFT)

# frames_window.mainloop()


#-------------------new windows--------------------------#
# from tkinter import *

# def create_window():
#   # new_window= Toplevel() #Toplevel()-->> new window 'on top' of other windows, linked to a 'bottom' window, (if 'bottom' window closes 'top' window is automatically close)
#   new_window=Tk() #this creats a new independent window
#   newWindow_window.destroy() #this will close out old window
# newWindow_window = Tk()

# Button(newWindow_window,text='create new window',command=create_window).pack()

# newWindow_window.mainloop()


#-----------------new window tabs-----------------------#
# from tkinter import *
# from tkinter import ttk

# tabs_window = Tk()

# notebook = ttk.Notebook(tabs_window) #widget that manages a collection of windows/displays
# tab1 = Frame(notebook) #new frame for tab1
# tab2 = Frame(notebook) #new frame for tab2

# notebook.add(tab1,text='Tab 1')
# notebook.add(tab2,text='Tab 2')
# notebook.pack(expand=True, #expand -->> this will expand to fill any spaces otherwise used
#               fill='both' #will fill space on a and y axis
# )
# Label(tab1,text='Hello this is tab number 1',width=50,height=25).pack()
# Label(tab2,text='goodbye this is tab number 1',width=50,height=25).pack()

# tabs_window.mainloop()


 #-------------grid geometry manager--------------------#
# from tkinter import *
# #grid()--->>geometry manager that organizes widgets in a table like structure in a parent

# def grid_submit():
#   print()

# grid_window = Tk()

# titleLable = Label(text='Enter you Info',font=('Arial',25)).grid(row=0,column=0,columnspan=2)

# firstNameLabel = Label(grid_window,text='first name: ',width=20,bg='red').grid(row=1,column=0)
# firstName_entry = Entry(grid_window).grid(row=1,column=1)

# lastNameLabel = Label(grid_window,text='last name: ',bg='green').grid(row=2,column=0)
# lastName_entry = Entry(grid_window).grid(row=2,column=1)

# EmailLabel = Label(grid_window,text='Email: ',bg='blue',width=30).grid(row=3,column=0)
# Email_entry = Entry(grid_window).grid(row=3,column=1)

# grid_submit_btn = Button(grid_window,text='submit',command=grid_submit).grid(row=4,column=0,columnspan=2)

# grid_window.mainloop()


#--------------progress bar---------------------------#
# from tkinter import *
# from tkinter.ttk import *
# import time

# def startDownload():
#   GB = 50
#   download = 0
#   speed =2
#   while(download < GB):
#     time.sleep(0.05) #wait 1sec to complete
#     first_bar['value'] += ((speed/GB)*100) #every time button clicks it fills by 10 percent
#     download += speed
#     percent.set(str(int((download/GB)*100))+"%")
#     progressbar_window.update_idletasks() #to automatically update the window
#     text.set(str(download)+"/"+str(GB)+" GB completed.")

# progressbar_window = Tk()

# percent = StringVar() #to update 'percent' with some string texts
# text = StringVar()

# first_bar = Progressbar(progressbar_window,orient=HORIZONTAL,length=300)
# first_bar.pack(pady=10)

# percentLabel = Label(progressbar_window,textvariable=percent).pack()

# taskLabel = Label(progressbar_window,textvariable=text).pack()

# download_btn = Button(progressbar_window,text='download',command=startDownload).pack()

# progressbar_window.mainloop()


#---------------------canvas-->>widget that is used to draw graphs, plots, images in a window----------------#
# from tkinter import *
# canvas_window = Tk()

# first_canvas = Canvas(canvas_window,height=500,width=500)
# # first_canvas.create_line(0,0,500,500,fill='blue',width=5) #(start x, start y, end x, end y)
# # first_canvas.create_line(0,500,500,0,fill='red',width=5) 
# # first_canvas.create_rectangle(50,50,250,250,fill='purple')

# # points = [250,0,500,500,0,500]
# # first_canvas.create_polygon(points,fill='yellow',outline='black',width=5)

# # first_canvas.create_arc(0,0,500,500,style=PIESLICE,start=270,extent=180) #arc is curved line between two points

# #--simple pokebole--#
# first_canvas.create_arc(0,0,500,500,fill='red',extent=180,width=10)
# first_canvas.create_arc(0,0,500,500,fill='white',start=180,extent=180,width=10)
# first_canvas.create_oval(190,190,310,310,fill='white',width=10)

# first_canvas.pack()
# canvas_window.mainloop()


#---------------key events----------------------------#
# from tkinter import *

# def doSomething(event):
#   # print('you pressed: '+ event.keysym)
#   keyEvents_label.config(text = event.keysym)

# keyEvents_window = Tk()

# # keyEvents_window.bind('<q>',doSomething) #(event(name of the button),functionName)
# #"<Return>"-->>enter key
# #"<q>"-->> 'q' key

# keyEvents_window.bind('<Key>',doSomething)

# keyEvents_label = Label(keyEvents_window,font = ("Helvetica",100))
# keyEvents_label.pack()

# keyEvents_window.mainloop()



#--------------mouse events-----------------------------#
# from tkinter import *

# def doSomething(event): #argument is "<Button-1>"
#   print('mouse cordinaties(where we clicked using mouse on the window: )' + str(event.x)+","+str(event.y))

# mouseEvents_window = Tk()

# #"<Button-1>"-->> left mouse button
# #"<Button-2>"-->>  mouse wheel(click)
# #"<Button-3>"-->>  right mouse button
# #"<ButtonRelease>"-->>  realeasing a mouse button
# #"<Enter>"-->>  just hover on the window by mouse(mouse entering to the window)
# #"<Leave>"-->>  mouse leaving the window
# #"<Motion>"-->>  where the mouse moved - best for games

# mouseEvents_window.bind("<Motion>", doSomething)

# mouseEvents_window.mainloop()


#----------------drag & drop widgets--------------------#
# from tkinter import *

# def drag_start(event):
#   widget = event.widget #to make it work for every widget this function includes

#   widget.startX = event.x 
#   #dragdrop_label.startX-->> the place we clicked on the label itself

#   widget.startY = event.y

# def drag_motion(event):
#   widget = event.widget
#   x = widget.winfo_x() - widget.startX + event.x
#    #dragdrop_label.winfo_x()-->>top left corner x place relative to the window

#   y = widget.winfo_y() - widget.startY + event.y
#   widget.place(x=x,y=y)

# dragDrop_window = Tk()

# dragdrop_label = Label(dragDrop_window,bg="red",width=10,height=5)
# dragdrop_label.place(x=0,y=0)

# dragdrop_label2 = Label(dragDrop_window,bg="blue",width=10,height=5)
# dragdrop_label2.place(x=100,y=100)

# #binding the label
# dragdrop_label.bind("<Button-1>",drag_start)
# dragdrop_label.bind("<B1-Motion>",drag_motion)

# #binding the label 2
# dragdrop_label2.bind("<Button-1>",drag_start)
# dragdrop_label2.bind("<B1-Motion>",drag_motion)

# dragDrop_window.mainloop()



#-------moving an image on window an canvas------------#
#-----------on window------------#
# from tkinter import *

# def move_up(event):
#   myimage_label.place(x=myimage_label.winfo_x(),y=myimage_label.winfo_y()-10)

# def move_down(event):
#   myimage_label.place(x=myimage_label.winfo_x(),y=myimage_label.winfo_y()+10)

# def move_left(event):
#   myimage_label.place(x=myimage_label.winfo_x()-10,y=myimage_label.winfo_y())

# def move_right(event):
#   myimage_label.place(x=myimage_label.winfo_x()+10,y=myimage_label.winfo_y())

# imagemove_window = Tk()

# imagemove_window.geometry("500x500")

# imagemove_window.bind("<w>",move_up)
# imagemove_window.bind("<s>",move_down)
# imagemove_window.bind("<a>",move_left)
# imagemove_window.bind("<d>",move_right)

# #for arrow keys
# imagemove_window.bind("<Up>",move_up)
# imagemove_window.bind("<Down>",move_down)
# imagemove_window.bind("<Left>",move_left)
# imagemove_window.bind("<Right>",move_right)

# myimage = PhotoImage(file='images/racingcar.png')
# myimage_label = Label(imagemove_window,image=myimage)
# myimage_label.place(x=0,y=0)

# imagemove_window.mainloop()

#-----------on canvas------------#
# from tkinter import *

# def move_up_canvas(event):
#    moveimage_canvas.move(myimage,0,-10)

# def move_down_canvas(event):
#    moveimage_canvas.move(myimage,0,10)

# def move_left_canvas(event):
#    moveimage_canvas.move(myimage,-10,0)

# def move_right_canvas(event):
#    moveimage_canvas.move(myimage,10,0)

# moveimage_canvas_window = Tk()

# moveimage_canvas_window.bind("<w>",move_up_canvas)
# moveimage_canvas_window.bind("<s>",move_down_canvas)
# moveimage_canvas_window.bind("<a>",move_left_canvas)
# moveimage_canvas_window.bind("<d>",move_right_canvas)

# #arrow keys
# moveimage_canvas_window.bind("<Up>",move_up_canvas)
# moveimage_canvas_window.bind("<Down>",move_down_canvas)
# moveimage_canvas_window.bind("<Left>",move_left_canvas)
# moveimage_canvas_window.bind("<Right>",move_right_canvas)

# moveimage_canvas = Canvas(moveimage_canvas_window,width=500,height=500)
# moveimage_canvas.pack()

# photoimage = PhotoImage(file="images/racingcar.png")
# myimage = moveimage_canvas.create_image(0,0,image=photoimage,anchor=NW)

# moveimage_canvas_window.mainloop()


#-----------------simple 2D animations------------------#
# from tkinter import *
# import time

# #constant(names should be all upper case[not that necessary but a common thing])-->> variables that are not changing throughout the process
# WIDTH = 500
# HEIGHT = 500
# xVelocity = 3
# yVelocity = 2 #velocity = speed

# animation_window = Tk()

# animation_canvas = Canvas(animation_window,width=WIDTH, height=HEIGHT)
# animation_canvas.pack()

# background_img = PhotoImage(file='images/earth.png')
# my_background_img = animation_canvas.create_image(0,0,image=background_img,anchor=NW)

# photo_img = PhotoImage(file='images/racingcar.png')
# my_img = animation_canvas.create_image(0,0,image=photo_img,anchor=NW)

# #getting height & the width of my_img
# img_width = photo_img.width()
# img_height = photo_img.height()

# while True:
#   coordinates = animation_canvas.coords(my_img)
#   print(coordinates)
#   if(coordinates[0] >= (WIDTH - img_width) or coordinates[0] < 0):
#     xVelocity = -xVelocity
#   if(coordinates[1] >= (HEIGHT - img_height) or coordinates[1] < 0):
#     yVelocity = -yVelocity

#   animation_canvas.move(my_img,xVelocity,yVelocity) #(image name, x speed, y speed)
#   animation_window.update()
#   time.sleep(0.01)

# animation_window.mainloop()


#--------------------animating multiple objects--------#
# from tkinter import*
# from Ball import *
# import time

# animate_multiple_window = Tk()

# WIDTH = 500
# HEIGHT = 500

# animate_multiple_canvas = Canvas(animate_multiple_window,width=WIDTH, height=HEIGHT)
# animate_multiple_canvas.pack()

# volley_ball = Ball(animate_multiple_canvas,0,0,100,1,1,"white")
# tennis_ball = Ball(animate_multiple_canvas,0,0,50,4,3,"yellow")
# basket_ball = Ball(animate_multiple_canvas,0,0,125,8,7,"orange")

# while True:
#   volley_ball.move()
#   tennis_ball.move()
#   basket_ball.move()
#   animate_multiple_window.update()
#   time.sleep(0.01)

# animate_multiple_window.mainloop()


#------------------clock GUI program--------------------#
# from tkinter import *
# from time import *

# def update():
#   time_string = strftime("%I:%M:%S %p")
#   time_label.config(text=time_string)

#   day_string = strftime("%A")
#   day_label.config(text=day_string)

#   date_string = strftime("%B %d, %Y")
#   date_label.config(text=date_string)

#   clockprogram_window.after(1000,update) #1000->mili secs, 'update'->will do the update every 1000 mili-secs

# clockprogram_window = Tk()

# time_label = Label(clockprogram_window,font=("Arial",50),fg="#00FF00",bg="black")
# time_label.pack()

# day_label = Label(clockprogram_window,font=("Ink Free",25))
# day_label.pack()

# date_label = Label(clockprogram_window,font=("Ink Free",30))
# date_label.pack()

# update()

# clockprogram_window.mainloop()


#----------------------sending an email-----------------#
# import smtplib #Simple Mail Transfer Protocol Library

# sender = "naksathaudage2000@gmail.com"
# receiver = "naduni.20191206@iit.ac.lk"
# password = "fbi0778593462"
# subject = "Python email text"
# body = "I wrote an Email :D"

# message = f"""From: Snoop Dogg{sender}
# To: Nicholas Cage{receiver}
# Subject: {subject}\n
# {body}
# """ #triple quotes-->> to get multiple lines of texts

# server = smtplib.SMTP("smtp.gmail.com", 587) #587 pot number->default mail submission port
# server.starttls() #start transport layer security

# #download an app to make the gmail less secure or else won't work
# try:
#   server.login(sender,password)
#   print("loged in...")
#   server.sendmail(sender,receiver,message) #to send an email
#   print("Email has been sent!")

# except smtplib.SMTPAuthenticationError:
#   print("unable to sign in")


#-------runing a python file using command prompt-------#
# #1. save file as .py(python file)
# #2. go tocommand prompt
# #3. navigate to directory w/ your file : cd C:\Program Files
# #invoke python interpreter + script: python hello_world.py

# print('hellow world')
# name = input("What's your name?: ")
# print("Hellow "+name)


#-------------------'pip for python'-------------------#
#pip = package manager for packages and modules from python package index
#****************************************************
#included for python versions 3.4+
#open command prompt
#
#help: pip
#check: pip --version
#update: pip install --upgrade pip
#installed packages: pip list
#check outdated packages: pip list --outdated
#install a package: pip install "package name"
#*****************************************************


#--------converting python file to an executable--------#
# (windows defender may prevent you from running)
# (make sure pip and pyinstaller are installed/updated)

# cd to directory that contains your .py file
# pyinstaller..
#     -F (all in 1 file)
#     -w (removes terminal window)
#     -i icon.ico (adds custom icon to .exe)   ('icon.ico'-->>icon means name of the ico file)
#     clock.py (name of your main python file)

# .exe is located in the dist folder
#i couldn't do upper progra cause of a 'pyinstaller' issue


#-------------------basic calculator--------------------#
# from tkinter import *

# def button_press(num):
#   global equation_text
#   equation_text = equation_text + str(num)
#   equation_label.set(equation_text)

# def equals():
#   global equation_text

#   try:
#     total = str(eval(equation_text)) #eval()-->>parse the expression we pass in
#     equation_label.set(total)
#     equation_text = total
#   except SyntaxError:
#     equation_label.set('arithmetic error')
#     equation_text = ""
#   except ZeroDivisionError:
#     equation_label.set('arithmetic error')
#     equation_text = ""

# def clear():
#   global equation_text
#   equation_label.set("")
#   equation_text =""

# cal_window =Tk()
# cal_window.title("Calculator program")
# cal_window.geometry("500x500")

# equation_text = ""
# equation_label = StringVar()

# label = Label(cal_window,textvariable=equation_label,font=('consolas',20),bg="white",width=24,height=2)
# label.pack()

# frame = Frame(cal_window)
# frame.pack()

# btn1 = Button(frame,text=1,height=4,width=9,font=35,command= lambda: button_press(1))
# btn1.grid(row=0,column=0)

# btn2 = Button(frame,text=2,height=4,width=9,font=35,command= lambda: button_press(2))
# btn2.grid(row=0,column=1)

# btn3 = Button(frame,text=3,height=4,width=9,font=35,command= lambda: button_press(3))
# btn3.grid(row=0,column=2)

# btn4 = Button(frame,text=4,height=4,width=9,font=35,command= lambda: button_press(4))
# btn4.grid(row=1,column=0)

# btn5 = Button(frame,text=5,height=4,width=9,font=35,command= lambda: button_press(5))
# btn5.grid(row=1,column=1)

# btn6 = Button(frame,text=6,height=4,width=9,font=35,command= lambda: button_press(6))
# btn6.grid(row=1,column=2)

# btn7 = Button(frame,text=7,height=4,width=9,font=35,command= lambda: button_press(7))
# btn7.grid(row=2,column=0)

# btn8 = Button(frame,text=8,height=4,width=9,font=35,command= lambda: button_press(8))
# btn8.grid(row=2,column=1)

# btn9 = Button(frame,text=9,height=4,width=9,font=35,command= lambda: button_press(9))
# btn9.grid(row=2,column=2)

# btn0 = Button(frame,text=0,height=4,width=9,font=35,command= lambda: button_press(0))
# btn0.grid(row=3,column=0)

# plus_btn= Button(frame, text='+',height=4,width=9,font=35,command= lambda: button_press('+'))
# plus_btn.grid(row=0,column=3)

# minus_btn= Button(frame,text='-',height=4,width=9,font=35,command= lambda: button_press('-'))
# minus_btn.grid(row=1,column=3)

# multiply_btn= Button(frame,text='X',height=4,width=9,font=35,command= lambda: button_press('*'))
# multiply_btn.grid(row=2,column=3)

# divide_btn= Button(frame,text='/',height=4,width=9,font=35,command= lambda: button_press('/'))
# divide_btn.grid(row=3,column=3)

# equal_btn= Button(frame,text="=",height=4,width=9,font=35,command= equals)
# equal_btn.grid(row=3,column=2)

# decimal_btn= Button(frame,text=".",height=4,width=9,font=35,command= lambda: button_press('.'))
# decimal_btn.grid(row=3,column=1)

# clear_btn= Button(cal_window,text="clear",height=4,width=12,font=35,command= clear)
# clear_btn.pack()

# cal_window.mainloop()



#--------------basic text editor------------------------#
# import os
# from tkinter import *
# from tkinter import filedialog, colorchooser, font
# from tkinter.messagebox import *
# from tkinter.filedialog import *

# def change_color():
#   color = colorchooser.askcolor(title="pick a color...or else")
#   text_area.config(fg=color[1])

# def change_font(*args):
#   text_area.config(font=(font_name.get(),size_box.get()))

# def new_file():
#   texteditor_window.title("Untitled")
#   text_area.delete(1.0, END)

# def open_file():
#   file = askopenfilename(defaultextension=".txt",file=[("All Files","*.*"),("Text Documents","*.txt")])

#   try:
#     texteditor_window.title(os.path.basename(file)) #title change according to the file's title we opened
#     text_area.delete(1.0,END)

#     file = open(file,"r")
#     text_area.insert(1.0,file.read())
#   except Exception:
#     print("Couldn't read file")
#   finally:
#     file.close()

# def save_file():
#   file = filedialog.asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text documents","*.txt")])

#   if file is None:
#     return
#   else:
#     try:
#       texteditor_window.title(os.path.basename(file))
#       file = open(file,"w")
#       file.write(text_area.get(1.0,END))
#     except Exception:
#       print("couldn't save file")
#     finally:
#       file.close()
  

# def cut():
#   text_area.event_generate("<<Cut>>")

# def copy():
#   text_area.event_generate("<<Copy>>")

# def paste():
#   text_area.event_generate("<<Paste>>")

# def about():
#   showinfo("About this program","This is a program written by YOUUUUUU !!!!") #(title,text)

# def quit():
#   texteditor_window.destroy()

# texteditor_window = Tk()

# texteditor_window.title("Text editor program")
# file = None

# window_width = 500
# window_height = 500
# screen_width = texteditor_window.winfo_screenwidth()
# screen_height = texteditor_window.winfo_screenheight()

# x = int((screen_width/2) - (window_width/2))
# y = int((screen_height/2) - (window_height/2))

# #making it more center
# texteditor_window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))

# font_name = StringVar(texteditor_window)
# font_name.set("Arial")

# font_size = StringVar(texteditor_window)
# font_size.set("25")

# text_area = Text(texteditor_window,font=(font_name.get(),font_size.get()))

# scroll_bar = Scrollbar(text_area)
# #allow the text area to expand
# texteditor_window.grid_rowconfigure(0, weight=1)
# texteditor_window.grid_columnconfigure(0, weight=1)
# text_area.grid(sticky=N + E + S + W) #to expand throught all areas
# scroll_bar.pack(side=RIGHT, fill=Y)
# text_area.config(yscrollcommand=scroll_bar.set)

# frame = Frame(texteditor_window)
# frame.grid()

# color_btn = Button(frame,text = "color", command = change_color)
# color_btn.grid(row=0,column=0)

# font_box = OptionMenu(frame,font_name, *font.families(), command = change_font) #return all the different fonts available to us
# font_box.grid(row=0,column=1)

# size_box = Spinbox(frame, from_ = 1, to=100, textvariable=font_size,command=change_font)
# size_box.grid(row=0, column=2)

# #dropdown
# menu_bar = Menu(texteditor_window)
# texteditor_window.config(menu=menu_bar)

# file_menu = Menu(menu_bar, tearoff =0)
# menu_bar.add_cascade(label = "file", menu = file_menu)
# file_menu.add_command(label = "New", command=new_file)
# file_menu.add_command(label = "Open", command=open_file)
# file_menu.add_command(label = "Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label = "Quit", command=quit)


# edit_menu = Menu(menu_bar, tearoff =0)
# menu_bar.add_cascade(label = "Edit", menu = edit_menu)
# edit_menu.add_command(label = "Cut", command=cut)
# edit_menu.add_command(label = "Copy", command=copy)
# edit_menu.add_command(label = "Paste", command=paste)

# help_menu = Menu(menu_bar, tearoff =0)
# menu_bar.add_cascade(label = "Help", menu = help_menu)
# help_menu.add_command(label = "About", command=about)


# texteditor_window.mainloop()



#--------------------tic-tac-toe game-------------------#
# from tkinter import *
# import random

# def next_turn(row,column):
#   global player #to get access to the player
#   if buttons[row][column]['text'] == "" and check_winner() is False:
#     if player == players[0]:
#       buttons[row][column]['text'] = player
#       if check_winner() is False:
#         player = players[1]
#         label.config(text=(players[1] + " turn"))
#       elif check_winner() is True:
#         label.config(text=(players[0]+ " wins"))
#       elif check_winner() == "Tie":
#         label.config(text=("Tie!"))

#     else:
#       buttons[row][column]['text'] = player
#       if check_winner() is False:
#         player = players[0]
#         label.config(text=(players[0] + " turn"))
#       elif check_winner() is True:
#         label.config(text=(players[1]+ " wins"))
#       elif check_winner() == "Tie":
#         label.config(text=("Tie!"))


# def check_winner():
#   for row in range(3):
#     if buttons[row][0]['text'] == buttons[row][1]['text'] ==buttons[row][2]['text'] != "":
#       buttons[row][0].config(bg="green")
#       buttons[row][1].config(bg="green")
#       buttons[row][2].config(bg="green")

#       return True
#   for column in range(3):
#     if buttons[0][column]['text'] == buttons[1][column]['text'] ==buttons[2][column]['text'] != "":
#       buttons[0][column].config(bg="green")
#       buttons[1][column].config(bg="green")
#       buttons[2][column].config(bg="green")
#       return True
  
#   if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#     buttons[0][0].config(bg="green")
#     buttons[1][1].config(bg="green")
#     buttons[2][2].config(bg="green")
#     return True
  
#   elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#     buttons[0][2].config(bg="green")
#     buttons[1][1].config(bg="green")
#     buttons[2][0].config(bg="green")
#     return True
  
#   elif empty_spaces() is False:
#     for row in range(3):
#       for column in range(3):
#         buttons[row][column].config(bg="yellow")
#     return "Tie"
  
#   else:
#     return False
  

# def empty_spaces():
#   spaces = 9
#   for row in range(3):
#     for column in range(3):
#       if buttons[row][column]['text'] != "":
#         spaces -= 1
#   if spaces ==0:
#     return False
#   else:
#     True

# def new_game():
#   global player
#   player = random.choice(players)
#   label.config(text=player + " turn")

#   for row in range(3):
#     for column in range(3):
#       buttons[row][column].config(text="",bg="#F0F0F0")


# tictac_window = Tk()

# tictac_window.title("Tic-Taca-Toe")
# players = ["x","o"]
# player = random.choice(players)
# buttons = [[0,0,0], #[[firstrow],[secondrow],[thirdrow]]
#            [0,0,0],
#            [0,0,0]]

# label = Label(text = player + " turn",font=('consolas',40))
# label.pack(side ="top")

# reset_btn = Button(text="restart",font=('consolas',20),command=new_game)
# reset_btn.pack(side="top")

# frame = Frame(tictac_window)
# frame.pack()

# for row in range(3):
#   for column in range(3):
#     buttons[row][column] = Button(frame, text="",font=('consolas',40),width=5,height=2,command= lambda row=row,column= column:next_turn(row,column))
#     buttons[row][column].grid(row=row,column=column)

# tictac_window.mainloop()

import coverter
from coverter import lbs_to_kg
import math
import random
from utlis import find_max
# import from pacage
# from ecommerce import shipping

from pathlib import Path
import ecommerce.shipping
from ecommerce.shipping import calc_shipping




# importing file from pathlib

path = Path()
for file in path.glob('*'):
    print(file)

# print(path.rmdir())
# ecommerce.shipping.calc_shipping()
# calc_shipping()
# calc_shipping()
# calc_shipping()
# print(lbs_to_kg(100))

# print(coverter.kg_to_lbs(70))

# numbers  = [10,90,100,2]
# maximum = find_max(numbers)

# print(maximum)

# # getting random 

# for i in range(5):
#     print(random.random())
#     print(random.randint(10,20))

# members = ['Bola', 'Kemi', 'Titi' ,'niyi']
# print(random.choice(members))

# class Dice:
#      def roll(self):
#          first =  random.randint(1,6)
#          second = random.randint(1,6)
#          return (first, second)


# dice = Dice() 
# print(dice.roll())    
# print(dice.first, dice.second)    

# print( 'hello word' * 10)
# #  Variable name
# student_count = 1000

# print(student_count)
# # interger
# rating = 10.1
# print(rating)
# # boolean
# is_publish = False
# print(is_publish)
# # string
# course_name = "Learing Python"
# print(course_name)

# # length built in function
# print(len(course_name))
# print(course_name[0])
# print(course_name[-1])
# print(course_name[0:3])
# print(course_name[0:])
# print(course_name[:])
# print(course_name[:3])

# # excape character
# #  breakin yhe line
# course = 'Python \nProgramming'
# # allow coate to show
# course1= 'Python \'Programming'
# # allow backsplash to show
# course2= 'Python \\Programming'
# print(course)
# print(course1)
# print(course2)

# # concatenate in python
# first = 'Muhmin'
# last = 'Soliu'
# full = first + " " + last
# all = f" {len(first)} {last}"
# print(full)
# print(all)
# print(first.upper())

# # Addional
# print (10 + 3)
# print (10 - 3)
# print (10 * 3)
# print (10 / 3)
# print (10 // 3)
# print (10 % 3)
# print (10 ** 3)
# x = 10
# x + 3
# x += 3
# print(x)

# #  ANother set of bult in function
# print(round(3.10))
# print(abs(-290))
# x  = 30.0
# print(math.ceil(2.9))

# # input function
# # falsey value
# print(bool(0))
# print(bool(""))
# print(bool())
# # condinal statement
# temperature = 10 
# if temperature > 30:
#     print("it too cold")
#     print("It nice weather")
# elif temperature > 20:
#     print("It managable")

# else: 
#     print('its hot')
# print("done")
# age = 18
# message = "quolify" if age >= 16 else "not qualify" 
# print (message)
  

# #   The And The Or . the Not operator

# is_current = True
# student = False
# is_qualify = False

# if (is_current or is_qualify ) and not student:
#     print("Eligeble")
# else:
#     print("Not Eligeble")
    
#     # chaining comparism operator
# age = 20
# if 18 <= age < 65:
#     # if age >= 18 and  age < 40:
#      print("Pass Test")

#     #  loop in python 
# for number in range(3) : 
#  print ("Otilo",(number + 1) * ".")  

# #  While loop
# command = ""
# while command  != "quit":
#     command = input('>')
#     print("Motogbo", command)
# count = 0
# for number  in range(1, 10) :
#     if number % 2 == 0:
#      count += 1
#      print( number ) 
# print(f"We have  {count} even number")  

# # function in python
# def greet(first, last):
#     print(f"{first} {last}")
#     print(" Welcome on Board")


# greet('', "Bola")
# greet("Niyi", "")
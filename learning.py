# # phone = input("Phone: ")
# # digital_mapping = {
# #     "1": "one",
# #     "2": "two",
# #     "3": "three",
# #     "4": "four"
# # }
# # outPut = ""
# # for ch in phone:
# #     outPut += digital_mapping.get(ch, "!") + " "
# #     # print(digital_mapping.get(ch, "!"), end=" ")
# # print(outPut)

# # message = input(">")
# # words = message.split(" ")
# # emojis = {
# #     ":)": "😊",
# #     ":(": "😒"
# # }
# # outPut = ""
# # for word in words:
# #     outPut += emojis.get(word, word) + " "
# #     # print(emojis.get(word, word), end=" ")
# # print(outPut)

# # function

# def greeting(name):
#     print(f"Hello { name}")
#     print(f"Welcome on Board")
#     print(f"Have a nice day {name}")
# greeting("Muhmin")
# print("Muhmin")
# print("Ali")

# def square(number):
#     return number * number


# # print(number * number)
# result = square(3)
# print(result)

# # class in python

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print("Move")

#     def draw(self):
#         print("Draw")
# point1 =  Point(10, 20)
# # point1.x = 10
# # point1.y = 20
# point1.draw()
# point1.move()
# print(point1.x,point1.y)

# class Person:
#   def  __init__(self, name):
#     self.name = name


#   def talk(self):
#          print(f'Hi, I am {self.name} ')


# john = Person('fola bola')
# bola = Person('Lateef kehinde')
# john.talk()
# # john.name = 'fola'
# # john.me = 'bola'
# print(john.name)
# print(bola.name)

# # inheritants in class

# class Mammal:
#     def talk(self):
#         print('Im calling you')

# class Dog(Mammal):
#     pass
# class Rat(Mammal):
#     pass
# rat = Rat()

# rat.talk()
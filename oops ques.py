# import math
# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def perimeter(self):
#         return 2*math.pi*self.radius
#     def area(self):
#         return math.pi*self.radius*self.radius
# r=int(input("enter the radius"))
# object=circle(r)
# print("the perimeter is",object.perimeter())
# print("the area is",object.area())
# print("the radius is {}".format(object.radius))
# print("the area is {}".format(object.area))
# print("the perimeter is {}".format(object.perimeter))

# class Person:
#     def __init__(self, name,country, birth_year):
#         self.name = name
#         self.country=country
#         self.birth_year = birth_year
    # def cal

# Import the date class from the datetime module to work with dates
# from datetime import date

# # Define a class called Person to represent a person with a name, country, and date of birth
# class Person:
#     # Initialize the Person object with a name, country, and date of birth
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
    
#     # Calculate the age of the person based on their date of birth
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# # Example usage
# # Create three Person objects with different attributes
# person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
# person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
# person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# # Access and print the attributes and calculated age for each person
# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of_birth)
# print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of_birth)
# print("Age:", person2.calculate_age())

# print("\nPerson 3:")
# print("Name:", person3.name)
# print("Country:", person3.country)
# print("Date of Birth:", person3.date_of_birth)
# print("Age:", person3.calculate_age())
# class calculator:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         return self.x+self.y
#     def divide(self):
#         if y!=0:
#             return self.x/self.y
#         else:
#             return("this is not divisible")
#     def subtract(self):
#         return self.x-self.y
# x=int(input("enter the number"))
# y=int(input("enter the number"))
# object=calculator(x,y)
# print("the sum is",(object.add()))
# print("the subtract is ",(object.subtract()))
# print("the divide is",object.divide())


# class stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,item):
#         self.iems.append(items)
    



# class calculator:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def add(self):
#         return self.x+self.y
#     def mul(self):
#         return self.x/self.y
#     def sub(self):
#         return self.x-self.y
#     def divide(self):
#         return self.x/self.y
#     def modulo(self):
#         return self.x%self.y
#     def exponent(self):
#         return self.x**self.y
# x=int(input("enter the number"))
# y=int(input("enter the number"))
# object=calculator(x,y)
# print("the sum is-:",object.add())
# print("the mul is-:",object.mul())
# print("the sub is-:",object.sub())
# print("the divide is-:",object.divide())
# print("the modulo is-:",object.modulo())
# print("the exponent is-:",object.exponent())


# class calculator:
    # def (self,x,y):
    #     self.x=x
    #     self.y=y
#     def add(self,x,y):
#         return x+y
#     def mul(self,x,y):
#         return x/y
#     def sub(self,x,y):
#         return x-y
#     def divide(self,x,y):
#         return x/y
#     def modulo(self,x,y):
#         return x%y
#     def exponent(self,x,y):
#         return x**y
# x=int(input("enter the number"))
# y=int(input("enter the number"))
# object=calculator()
# print("the sum is-:",object.add(x,y))
# print("the mul is-:",object.mul(x,y))
# print("the sub is-:",object.sub(x,y))
# print("the divide is-:",object.divide(x,y))
# print("the modulo is-:",object.modulo(x,y))
# print("the exponent is-:",object.exponent(x,y))





# class india:
#     def capital(self):
#         return ("The capital of india is new delhi.")
#     def language(self):
#         return ("The Lang of india is hindi.")
#     def me(self):
#         return ("india is a Develpoed country.")
# class usa:
#     def capital(self):
#         return ("The capital of usa is washington.")
#     def language(self):
#         return ("The lang of usa is english.")
#     def me(self):
#         return ("usa is a developed country.")
# obj1=usa()
# obj2=india()
# print(obj1.capital())
# print(obj1.language())
# print(obj1.me())
# print(obj2.capital())
# print(obj2.language())
# print(obj2.me())


# class stack:
#     def __init__(self):
#         self.items=[]
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.pop()
#         else:
#             return "the stack is empty"
#     def is_empty(self):
#         return len(size.items)==0
#     def size(self):
#         return len(size.items)
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return "Empty stack."
# stack = stack()

# # Push items onto the stack
# stack.push(0)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print("Stack size:", stack.size())
# print("Top element:", stack.peek())

# # Pop an item from the stack, and print the popped item, and the updated size and top element
# popped_item = stack.pop()
# print("\nPopped item:", popped_item)
# print("\nStack size:", stack.size())
# print("Top element:", stack.peek())

# #----------------------------------------
# # Create another instance of the Stack class
# stack1 = Stack()

# # Print the size of the empty stack and attempt to pop an item (with an error message)
# print("\nStack size:", stack1.size())
# popped_item = stack1.pop()
# print("\nPopped item:", popped_item) 



# Define a class called Stack to implement a stack data structure
# class Stack:
#     # Initialize the stack with an empty list to store items
#     def __init__(self):
#         self.items = []

#     # Push an item onto the stack
#     def push(self, item):
#         self.items.append(item)

#     # Pop (remove and return) an item from the stack if the stack is not empty
#     def pop(self):
#         if not self.is_empty():
#             return self.pop()
#         else:
#             return "Cannot pop from an empty stack."

#     # Check if the stack is empty
#     def is_empty(self):
#         return len(self.items) == 0

#     # Get the number of items in the stack
#     def size(self):
#         return len(self.items)

#     # Peek at the top item of the stack without removing it, if the stack is not empty
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return "Empty stack."

# # Example usage
# # Create an instance of the Stack class
# stack = Stack()

# # Push items onto the stack
# stack.push(0)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# # Print the size of the stack and the top element
# print("Stack size:", stack.size())
# print("Top element:", stack.peek())

# # Pop an item from the stack, and print the popped item, and the updated size and top element
# popped_item = stack.pop()
# print("\nPopped item:", popped_item)
# print("\nStack size:", stack.size())
# print("Top element:", stack.peek())

# #----------------------------------------
# # Create another instance of the Stack class
# stack1 = Stack()

# # Print the size of the empty stack and attempt to pop an item (with an error message)
# print("\nStack size:", stack1.size())
# popped_item = stack1.pop()
# print("\nPopped item:", popped_item) 




# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# modelX = Vehicle(240, 18)
# # print(modelX.max_speed, modelX.mileage)
# print("the speed of car is",modelX.max_speed)
# print("the milege of the car is",modelX.mileage)




# class vehicle:
#     def __init__(self,max_speed,mileage,name):
#         self.max_speed=max_speed
#         self.mileage=mileage
#         self.name=name
# class bus(vehicle):
#     def me(self):
#         print("this is the bus")
# obj=vehicle(200,234,"school")
# print("this is the speed of the car",obj.max_speed)
# print("this is the mileage",obj.mileage)
# print("the name of the car is",obj.name)



# class vehicle:
#     color="white"
#     model=2015
#     def __init__(self,name,mileage):
#         self.name=name
#         self.mileage=mileage
# class bus(vehicle):
#         pass
# class car(vehicle):
        pass
# obj1=bus("audi",234)
# obj2=car("fortuner",235)
# obj3=vehicle('safari',20)
# # print("the name of the bus is {}".fromat(obj1.name),"the mileage of the vehicle is {}".format(obj1.mileage))
# obj1=vehicle("audi",234)

# print("the color of the car is:",obj1.color)
# print("the name of the car is:",obj1.name)
# print("the mileage of the car is:",obj1.mileage)
# print("the model of the car is:",obj1.model)
# # print("the color of the car is:",obj2.color)
# # print("the name of the bus is:",obj2.name)
# # print("the mileage of the bus is:",obj2.mileage)
# # print("the model of the car is:",obj2.model)
# print(type(obj1))
# print(isinstance(obj3,vehicle))#################doubt



# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())



# Import required modules
# from abc import ABC, abstractmethod

# # Create Abstract base class
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     # Create abstract method      
#     @abstractmethod
#     def printDetails(self):
#         pass
  
#     # Create concrete method
#     def accelerate(self):
#         print("Speed up ...")
  
#     def break_applied(self):
#         print("Car stopped")

# # Create a child class
# class Hatchback(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
  
#     def sunroof(self):
#         print("Not having this feature")

# # Create a child class
# class Suv(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)
  
#     def sunroof(self):
#         print("Available")

# # Create an instance of the Hatchback class
# car1 = Hatchback("Maruti", "Alto", 2022)
# car2=Suv("audi","fortuner",2024)
# # Call methods
# car1.printDetails()
# car1.accelerate()
# car1.sunroof()
# car1.break_applied()
# car2.Suv()


# import array
# for name in array.__dict__:
#     print(name)




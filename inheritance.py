# class Parent(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def disp(self):
#         print(self.name, self.age)
# k1=Parent("simran",23)
# k1.disp()

# class child(Parent):
#     def klm(self):
#         pass
# khushi=child("ram",12)
# khushi.disp()


# class khushi:
#     def __init__(re,age,name):
#         re.age=age
#         re.name=name
#     def yge(re):
#         print(re.age,re.name)
# l1=khushi(23,"simma")
# l1.yge()

# class child(khushi):
#     def kjsj(re):
#         print("ew gavsfdcs")
# ii=child(24,"kahsub")
# ii.yge()

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


# class Person(object):

# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def noEmployee(self):
# 		return False


# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isemploy(self):
# 		return True


# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee())
# ii


# class khushi:
# 	def __init__(self,name):
# 		self.name=name
# obj=khushi("simran")
# print("my name is {}".format(obj.name))

# class B(khushi):
# 	def __init__(self)
# obj

# class Animal:

#     # attribute and method of the parent class
#     name = ""
    
#     def eat(self):
#         print("I can eat")

# # inherit from Animal
# class Dog(Animal):

#     # new method in subclass
#     def __init__(self):
#         # access name attribute of superclass using self
#         self.name=name
#     def display(self):    
#         print("My name is ", self.name)

# # create an object of the subclass
# labrador = Dog("rohu")

# # # access superclass attribute and method 
# # # labrador.name = "Rohu"
# # labrador.eat()

# # call subclass method 
# labrador.display()

#inheritance concept= 1. single level
# class Animal:
#     def eat(self):
#         print("i can eat")
# class Dog(Animal):
#     def __init__(self,name):
#         self.name=name
#         print("my name is :",self.name) 
# jj=Dog("rohu")
# jj.eat()


# class Father:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class Son(Father):
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# obj1=Father("anjum",2000)
# obj=Son("simran",9000)
# print("my name is {},my salary is {}".format(obj1.name,obj1.salary))        
# print("my name is {},my salary is {}".format(obj.name,obj.salary))               
#multilevel inheritance


# class Hello:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# class Yellow(Hello):
#     def __init__(self,name,roll,age):
#         super().__init__(name,roll) 
#         self.age=age
# class Wellow(Yellow):
#     def __init__(self,name,age,roll):
#         super().__init__(name,roll,age)
#     def display(self):
#         print("this is the name :",self.name) 
#         print("this is the age :",self.age)
#         print("this is the roll :",self.roll) 
# kite=Wellow("lokesh",23,45)
# kite.display()          


# class Base:
# 	# Constructor to set Data
# 	def __init__(self, name, roll, role):
# 		self.name = name
# 		self.roll = roll
# 		self.role = role



# class Base:
# 	# Constructor to set Data
# 	def __init__(self, name, roll, role):
# 		self.name = name
# 		self.roll = roll
# 		self.role = role

# # Intermediate Class: Inherits the Base Class
# class Intermediate(Base):
# 	# Constructor to set age
# 	def __init__(self, age, name, roll, role):
# 		super().__init__(name, roll, role)
# 		self.age = age

# # Derived Class: Inherits the Intermediate Class
# class Derived(Intermediate):
# 	# Method to Print Data
# 	def __init__(self, age, name, roll, role):
# 		super().__init__(age, name, roll, role)

# 	def Print_Data(self):
# 		print(f"The Name is : {self.name}")
# 		print(f"The Age is : {self.age}")
# 		print(f"The role is : {self.role}")
# 		print(f"The Roll is : {self.roll}")

# # Creating Object of Base Class
# obj = Derived(21, "Lokesh Singh", 25, "Software Trainer")

# # Printing the data with the help of derived class
# obj.Print_Data()




# class kk:
#     def __int__(self,name,role):
#         self.name=name
#         self.role=role
# class jj(kk):
#     def __init__(self,name,role,age):
#         super().__init__(name,role)
#         self.age=age
# class ii(kk):
#     def __init__(self,name,role,age):
#         super().__init__(name,role,age)
#     def display(self):
#         print("my name is:",self.name)
#         print("my role is:",self.role)
#         print("my age is:",self.age)
# obj=ii("khushi","manager",78)
# ii.display()




# # # MULTIPLE ONHERITANCE CONCEPT = IT MEANS THE CHILD INHERIT FROM HIS FATHER AND THE FATHER INHERIT FROM HIS FATHER MEANS MULTIPLE IS DONE ONE INHREIT FORM THEIR UPEER.
#CODE-:
# class khushi:
#     def kjsd(self):
#         print("welcome to our india")
# class simmi(khushi):
#     def kkk(self):
#         print("welcome to delhi")
# class simba(simmi):
#     def asd(self):
#         print("welcome to faridabd")
# obj=simba()
# obj.kjsd()
# obj.kkk()
# obj.asd()




# # # SINGLE INHERITANCE=HERE ONE OF THE CHILE IHERITS FROM THEIR FATHER. 
# class khushi:
#     def kjsd(self):
#         print("welcome to our india")
# class simmi(khushi):
#     def kkk(self):
#         print("welcome to delhi")
# obj=simmi()
# obj.kjsd()
# obj.kkk()




# # # Multilevel inheritance= it means that the child inherit the properties from his parents as well as feom the uncle or his chachu.
# class khushi:
#     def kjsd(self):
#         print("welcome to our india")
# class simmi:
#     def kkk(self):
#         print("welcome to delhi")
# class simba(simmi,khushi):
#     def asd(self):
#         print("welcome to faridabd")
# obj=simba()
# obj.kjsd()
# obj.kkk()
# obj.asd()


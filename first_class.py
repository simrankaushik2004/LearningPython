# single line of comments 
# print('heelo everyone we are learners')

# abc = int(input("enter the first  number"))
# print(type(abc))

# multiline comments 
'''a = 200
print(a)
a = 500                                                                        

print(a)'''

"""
hello everyone we are learners and we are learning
about new 
technology
like python with data science
and we are pursuing our graduation 
from aravali college of engineering as well as 
management """


# there are different types of data types in python 
Numeric types
dictionary types
set types
list types
tuple types
c

def checkPrime(max_num):
    """
    Check whether the given number is prime or not
    """
    for num in range (2, max_num):
        if max_num % num == 0:
            return False
    return True

def twinPrime(max_num):
    """
    Generates the list of twin primes
    """
    for first_num in range(2, max_num):
        second_num = first_num + 2
        if (checkPrime(first_num) and checkPrime(second_num)):
            print(" {0} and {1}".format(first_num, second_num))

print("Twin Prime: ")
twinPrime(1000)
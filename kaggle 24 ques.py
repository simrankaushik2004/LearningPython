# # table 
# x=int(input("enter the number"))
# def table():
#     for i in range(1,11):
#          print(x,"x",i,"=",x*i)
# table()



# # # # to make two consecutive odd numbers and twin prime numbers
# def check_primenum(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# def twin_prime(n):
#     for j in range(2,n):
#         k=j+2
#         if(check_primenum(j)and check_primenum(k)):
#             print("{0} and {1}".format(j,k))
# print("twin_prime: ")
# twin_prime(100)       


# x=int(input("enter the number"))
# def binarynum():
#     print(bin(x))
# binarynum()



# #find the max num from the given list
# x=[1,3,4,5,6,7,8,9,90]
# def maxnum():
#     print(max(x))
# maxnum()


# def checkPrime(max_num):
#     """
#     Check whether the given number is prime or not
#     """
#     for num in range (2, max_num):
#         if max_num % num == 0:
#             return False
#     return True

# def twinPrime(max_num):
#     """
#     Generates the list of twin primes
#     """
#     for first_num in range(2, max_num):
#         second_num = first_num + 2
#         if (checkPrime(first_num) and checkPrime(second_num)):
#             print(" {0} and {1}".format(first_num, second_num))

# print("Twin Prime: ")
# twinPrime(1000)




# #to d

# def prime_factors(n):
#     factors = []
#     divisor = 2
    
#     while divisor <= n:
#         if n % divisor == 0:
#             factors.append(divisor)
#             n //= divisor
#         else:
#             divisor += 1
    
#     return factors

# # Example usage:
# number = 56
# print(f"Prime factors of {number} are: {prime_factors(number)}")


# def factorial(x):
#     if x==0:
#         return 1
#     else:
#         return x*factorial(x-1)
# result=factorial(0)
# print(result)
# def permutations(x, r):
#     if x < r:
#         return 0
#     return factorial(x) // factorial(x - r)
# print(permutations(x, r))

# 1. Write a  Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# for i in range(1500,2700):
#     if i%7==0 and i%5==0:
#         print(i)
 
 
 
# F=input("enter the temperature")
    
# if temp==F:
#     C = (5/9) * (F - 32)
#     print(C)
# elif()
# else:
#      F = (9/5)*C + 32
#      print(F)
      
# x=int(input("enter the draw number"))
# if x>=1 and x<=9:
#     print("you are lucky and you win")
# else:
#     print("we are sorry to say that you lose this draw")

# n=int(input("enter the number of rows"))

# for i in range(0,n):
#     for j in range(0,i+1):
#         print('* ',end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(0,i-1):
#         print('* ',end="")
#     print()

# n=int(input("enter the number of rows"))

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("* ",end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(0,i-1):
#         print("* ",end="")
#     print()


# l=[1,2,"string",1+3j,23.5]
# for i in l:
#     print("type of", i ,"is",type(i))


# #Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# x=int(input("enter the number"))
# for i in range(1,50):
#     if x%3==0:
#         print("fizz")
#     if x%5==0:
#         print("buzz")
#     if x%5==0 and x%3==0:
#         print("fizzbuzz")
#     else:
#         print()


# result_str = ""
# # Iterate through rows from 0 to 6 using the range function
# for row in range(0, 7):
#     # Iterate through columns from 0 to 6 using the range function
#     for column in range(0, 7):
#         # Check conditions to determine whether to place '*' or ' ' in the result string
        
#         # If conditions are met, place '*' in specific positions based on row and column values
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str = result_str + "*"  # Append '*' to the 'result_str'
#         else:
#             result_str = result_str + " "  # Append space (' ') to the 'result_str'

#     result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'

# # Print the final 'result_str' containing the pattern
# print(result_str) 


# a=""
# for row in range(0,7):
#     for column in range(0,7):
#         if (((column==1 or column==5) and row!=0) or ((row==0 or row==3) and (column>1 and column<5))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)

# # f
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (((column==1)) or ((row==0 or row==3 ) and (column>1 and column<6))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
#     print(a)
             

# # # h
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (((column==1 or column==9) and row!=0) or ((row==3) and (column>1 and column<9))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
#     print(a)

# # for h
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (((column==1 or column==9) and row!=0) or ((row==3) and (column>1 and column<9))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)


# For m
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (((column==1 or column==9) ) or(row==2 or row==1)and ((row==0 or row==3) and (column>0 and column<7) or column==5 or column ==1) and (row==1 or row==2)):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)


# for p
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (column==1) or ((row==0 or row==3) and (column>0 and column<5) or ((column==5 or column ==1) and (row==1 or row==6))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)











# # to make two consecutive odd numbers and twin prime numbers
# def check_primenum():
#     for i in range(2,n):
#         n%i==0
#   

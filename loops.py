# #for loop in python
# # Create a list of items 
# items = ['pen', 'notebook', 
# 		'pencil', 'lunch box'] 

# # Run a loop to print 
# # items in a list 
# for item in items: 
#     print(item) 



# i=10
# # for i in range(10):
# #     print(i)


# # #for loop in range for print 
# # x=int(input("enter the value"))
# # for x in range(1,11):
# # #     print(x*x)


# i=input("enter the value")
# for x in range(1,100):
#     print(i*x)


# for i in range(1,100):
#     if i%2==0:
#         print(i)
        


# for i in range(1,100):
#     if i%2!=0:
#         print(i)



#doubt
# x=int(input("enter the value of x"))
# sum=0
# for i in range(1,x+1):
#     sum+=i
#     print(sum)



#     # if the given number is 10
# given_number = 10
 
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
 
# # since we want to include the number 10 in the sum
# # increment given number by 1 in the for loop
# for i in range(1,given_number+1):
#         sum+=i
 
# # print the total sum at the end
# print(sum)


# # # #Example 4: Python program to calculate the sum of all the odd numbers within the given range.

# sum=0
# for i in range(1,100):
#     if i%2==0:
#         sum+=i
        # print(sum)

# # if the given range is 10
# given_range = 10
 
# # set up a variable to store the sum
# # with initial value of 0
# sum = 0
 
# for i in range(given_range):
 
#         # if i is odd, add it
#         # to the sum variable
#         if i%2!=0:
#                 sum+=i
 
# # print the total sum at the end
# print(sum)


# #Example 8: Python program to check if the given string is a palindrome.
# x
# for i in range(1,11):
#     if i%x==0:
#         print('prime no',x)


# n=int(input("enter the number of rows"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")
#     print()


    
# for make u
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (((column==1 or column==9) and row!=0) or ((row==8 or row==6) and (column>1 and column<9))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)


# o

# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (column==1) or ((row==0 or row==3) and (column>0 and column<5) or ((column==5 or column ==1) and (row==1 or row==2))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)




# #for A square
# a=""
# for row in range(0,7):
#     for column in range(0,10):
#         if (((column==1 or column==9) and row!=0) or ((row==0 or row==6) and (column>1 and column<9))):
#             a=a+"*"
#         else:
#             a=a+" "
#     a =a +"\n"
# print(a)


# #reverse a string 
# list=input("enter the string:")
# def reverselist(char):
#     if char[::-1]==list:
#         return True
#     else:
#         return False
# print(reverselist(list))

# # while loop
# a=11
# while a>10:
#         print(a,"hellp")
#         a=a-1
# print(a)




w="hello how are you"
for i in w:
        print(i)

# #STRING FUNCTIONS
# # #1.upper()
# # t="simrn122"
# # # print(t.upper())
# # # print(t.lower())
# # # print(t.title())
# # # print(t.capitalize())
# # # print(t.find("l",4))
# # # print(t.index("s"))
# # print(t.isalpha())
# # print(t.isalnum())
# # print(t.isdigit())
# a=67;
# print(chr(a))
# f="C"
# # print(ord(f))

# txt1="welcome to {fname} {lname}".format(fname="our",lname="institute")


# txt2="welcome to {} {}".format("our","institute")


# txt3="welcome to {0:>10} {1}".format("our","institute")
# print(txt1)
# print(txt2)
# print(txt3)


# l=[1,2,3,5,6]
# for i in range(5):
#     print(l(i))
# l=[1,2,3,4]
# l1=[1,3,3,4]
# for m,n in zip(l,l1):
#     print(m,n)


# l="hello"
# # print(list(l ))
# k=l.split()
# print(k)

# k=[]
# for i in range(1,4):
#     m=input("enter the value" +str(i)+ "-:")
#     k.append(m)
# print(k)



# from speak import sum
# print(sum(10,30))
# # print(mul(10,20))



# factorial of a number

# x=int(input("enter"))
# factorial=1
# if x==0:
#     print("1")
# else:
#     for i in range(2,x+1):
#         factorial=i*factorial
#     print(factorial)



# num = int(input("Enter a number: "))    
# factorial = 1    
# # if num < 0:    
# #    print(" Factorial does not exist for negative numbers")    
# if num == 0:    
#    print("The factorial of 0 is 1")    
# else:    
#    for i in range(1,num+1):    
#        factorial = factorial*i    
#    print("The factorial of",num,"is",factorial)





from speak import *
print(sum(10,2,2,2,2,2,2,2))
print(mul(10,2,2,3,4,6,7,8))
print(sum(12,12,2,2,2,2,2,2))
print(sum(12,12,2,2,2,2,2,5))
print(mul(12,12,2,2,2,2,2,2))
print(sum(12,12,2,2,2,2,2,2))
# # a=(1,2,3,4,5,"anjum")
# # print(a,type(a))

# # # 2. Write a  Python program to create a tuple with different data types.
# # d=("simran",True,"anjum",2,3)
# # print(d,type(d))
# # # 3. Write a Python program to create a tuple of numbers and print one item.
# # # print(d[1])/

# # # 4. Write a Python program to unpack a tuple into several variables.
# # l=1,2,3,4,5
# # print(l)
# # n,m,k,e,r=l
# # print(n+m+k+e+r)


# # 5. Write a Python program to add an item to a tuple.
# # i=(1,2,3,4,5,6)
# # # print(i)
# # # i=i+(9,)
# # # print(i)

# # # list(i).append(10)
# # k=list(i)
# # # k.append(10)
# # print(k.append(10)or k)


# # # 6. Write a Python program to convert a tuple to a string.
# # p=("python","terve")
# # str='-'.join(p)m
# # print(str,type(str))


# # tup=(1,3,3,5,5,6,23,45,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6)
# # # print(s)
# # # x=s.count(6)
# # # y=s.count(5)
# # # print(x)
# # # print(y)
# # for i in tup:
# #     if tup.count(i) > 1:
# #         print(i)


# # # 10. Write a  Python program to check whether an element exists within a tuple.
# # h=("12345",7,8,9)
# # # print(h,type(h))
# # print(7 in h)

# # Create a tuple containing a sequence of items
# # tuplex = ("w", 3, "r",  "e", "s", "o", "u", "r", "c", "e")

# # # Check if the character "r" is present in the 'tuplex' tuple and print the result
# # print("r" in tuplex)

# # # Check if the number 5 is present in the 'tuplex' tuple and print the result
# # print(3 in tuplex)


# w=(1,2,3,5,6,78,"the")
# for i in w:
#     if i==123:
#         print("element is present")
# else:
#     pass


# list=[1,3,4,5,6]
# a=tuple(list)
# print(a)


# remove an item of an tuple
# x=(1,2,3,45,6)
# y=list(x)
# print(y)
# y.remove(4)
# print(y)

# print(x[::-2])
# # print(len(x))
# y=set(x)
# print(y)

# a=((1,"hello"),(2,"sir"))
# for x,y in a:
#     z=dict(a)
# print(z)
# # 
# a = ("John", "john", "Mike")
# b = ("Jenny", "Christy")

# x = zip(a, b)
# print(x)
# y=dict(x)
# print(y,type(y))


# # Create a tuple containing three num
# t = (100, 200, 300)

# # Use the 'format' method to insert the tuple 't' into the string and print the result
# c=print("this is tupple",t)
# print(c)
# print(type(c))



# # Create a tuple containing three numbers
# t = (100, 200, 300)
# # z=(1,3,4,6)
# # # Use the 'format' method to insert the tuple 't' into the string and print the result
# # print('This is a tuple')
# x=list(t)
# x[2]=12
# print(x)


# y=((),(),(1,2,3,4,5,67,7))
# # print(y,type(y))
# # z=list(y)
# # z.remove(())
# # print(z)
# for i in y:
#     if y==():
#         remove()
#         print(rom)

# L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]

# # Print the modified list 'L' after removing the empty tuples.
# L = [t for t in L if t]
# print(L) 
# y=(1,2,3,4,5,6789,0,7)
# x=list(y)
# print(x)
# x.sort()
# print(x)



# y.sort()
# print(y)

# o=[1,22,3,5,62,7]
# x=0
# for i in o:
#     x=x+1
#     if x<x+i:
#         print(x)
#     else:
#         print(x+i)
 
# x=(1,23,4,5,6,88,6)
# print(x)
# l=list(x)
# l.sort()
# print(l)
# z=l[::-1]
# print(z)

# p=[1,2,3,4,5,6,8,(2,3,4),33]
# x=p.count()
# print(x)
# print(len(p))
# print(tuple(p))

# 
# 
# /
# p=[1,2,3,4,5,6,8,(2,3,4),33]

# for i in p:
#     if isinstance(i, tuple):
#         break
#         x+=1
# print(x)
     
    #   a tuple.




# num = [10, 20, 30,40,56,556 (10, 20), 40]

# # Initialize a counter 'ctr' to keep track of the index of the first tuple in the list.
# ctr = 0

# # Iterate through each element 'n' in the 'num' list.
# for n in num:
#     # Check if 'n' is an instance of a tuple.
#     if isinstance(n, tuple):
#         # If 'n' is a tuple, exit the loop.
#         break
#     # Increment the counter 'ctr' for non-tuple elements.
#     ctr += 1

# # Print the value of the 'ctr' variable, which represents the index of the first tuple in the list.
# print(ctr) 

# # Create a list 'num' that contains a sequence of numbers and a tuple.
# num = [10,20,30,45,768,89, (10, 20), 40]

# # Initialize a counter 'ctr' to keep track of the index of the first tuple in the list.
# ctr = 0

# # Iterate through each element 'n' in the 'num' list.
# for n in num:
#     # Check if 'n' is an instance of a tuple.
#     if isinstance(n, tuple):
#         # If 'n' is a tuple, exit the loop.
#         break
#     # Increment the counter 'ctr' for non-tuple elements.
#     ctr += 1

# # Print the value of the 'ctr' variable, which represents the index of the first tuple in the list.
# print(ctr) 

p=(1,2,3,4,5,6,8,9,[2,3,4],33)
x=0
for i in p:
    if isinstance(i, list):
        break
    x=x+1
print(x)


# p="python"
# print(type(p))
# c=tuple(p)
# print(c,type(c))


# z=(1,2,3,-5,-9)
# result=1
# for i in z:
#     result=result*i
# print(result)


# p=(1,2,3)
# print(sum(p)/len(p))

# /tuple into a integer
# p=("1","2","3")
# print(int(p[0]),int(p[1]),int(p[2]))



# tuple into a integer in tuple
# p=("1","2","3")
#((int(p[0]),int(p[1]),int(p[2])))



 # Define a function named 'tuple_int_str' that takes a tuple of tuples 'tuple_str' as input.
# def tuple_int_str(tuple_str):
#     # Create a new tuple 'result' by converting the string elements in each inner tuple to integers.
#     result = tuple((int(x[0]), int(x[1])) for x in tuple_str)
    
#     # Return the resulting tuple.
#     return result

# # Create a tuple of tuples 'tuple_str' containing pairs of strings.
# tuple_str = (('333', '33'), ('1416', '55'))

# # Print a message indicating the original tuple values.
# print("Original tuple values:")

# # Print the 'tuple_str' tuple.
# print(tuple_str)

# # Print a message indicating the new tuple values, which are obtained by converting the strings to integers using the 'tuple_int_str' function.
# print("\nNew tuple values:")

# # Call the 'tuple_int_str' function to convert the strings to integers and print the result.
# print(tuple_int_str(tuple_str))



# p=(('333', '33'), ('1416', '55'),(12,34))
# def stringint(p):
#     result = tuple((int(x[0]), int(x[1])) for x in p)
#     return result
# print(stringint(p))


# p=(('333', '33'), ('1416', '55'),(12,34))
# def stringint(p):
#     result = (int(x[0]), int(x[1])) for x in p:
#     return result
# print(stringint(p))





# p=((12,98,12),(12,3,4,4),(34,45,56))
# def num(p):
#     # result = [sum(x) / len(x) for x in p]

#     return result
# print(num(p)) 



# p=(1,2,3,4,5,6,7,8,(1,2),(12,34))
# result=0
# for i in p:
#     if isinstance(i, tuple):
#         break
#     result=result+1
# print(result)



# def test(p):
#     result=map:sum,p
#     return list(result)
# l=(1,2,3,(2,3,4,5),(4,5,5))        
# print(test(l))


# p=(1,2,3,4)
# print(sum(p))

# p=[(1,3),(1,5)]




# def avg(first):
#     result=map(sum,first)
#     return list(result)
# p=((12,98,12),(12,3,4,4),(34,45,56))
# print(avg(p))

# def avg(first):
#     result=lambda:sum,first
#     return list(result)
# p=((12,98,12),(12,3,4,4),(34,45,56))
# print(avg(p))



# p="python ,simran"
# print(type(p))
# c=tuple(p)
# print(c,type(c))

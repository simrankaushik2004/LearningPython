# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for i in range(2,6):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=' ')
#     # new line after each row
#     print('')




# for i in range(0):
#     print(i)


# row=int(input("enter the value"))
# for i in range(row):
#     for j in range(i):
#         print(i,end="")
#     print()



# rows = 5
# for i in range(rows):
#     for j in range(1, i + 2):
#         print(i, end=' ')
#     print()
# # 
#it is an inverted pyramid starting from 12 and end on 1 because it is i.
# rows = 12
# for i in range(rows,0,-1):
#     for j in range(0,i):
#         print(i, end=' ')
# #     print()

# it is an inverted pyramid starting from 12 and end on 2 because it is i-1 if i=1 it becomes 0.
# rows = int(input("enter the number"))
# for i in range(rows,0,-1):
#     for j in range(i):
#         print(i, end=' ')
#     print()

# diect prit line by line from 1 to 12 
# rows = 12

# for i in range(rows):
#     for j in range(0,i):
#         print(i, end=' ')
#     print("")


# Another inverted half-pyramid pattern with a number 0 included
# rows = int(input("enter the number")) 
# for i in range(rows,0,-1):
#     for j in range(i):
#         print(j, end=' ')
#     print()


#for print pattern in same no of rows and column when we print j  than zero include otherwise not included

# rows = int(input("enter the number")) 
# for i in range(rows,0,-1):
#     for j in range(rows):
#         print(i, end=' ')
#     print()

# # print the number in fom of iverted pyramid after some distance
# rows = int(input("enter the number"))
# for i in range(1,rows):
#     for k in range(1,rows-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("3", end=' ') 
#     print()


# to print numberin for or triangle shape/diamond shape,arrow half, arrow full
rows = 15
for i in range(1,rows):
    for k in range(1,rows-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*", end=' ') 
    print()
for i in range(12):+


    for k in range(3,12):
        print(" ", end="")
    for j in range(7,11):
        print( "*",end=" ")
    print("")
rows =15
for i in range(rows,0,-1):
    for k in range(0,rows-i):
        print(" ",end="")
    for j in range(i-1):
        print("*", end=' ')
    print()   
# rows=15
# for i in range(rows,0,-1):
#     for k in range(0,rows-i):
#         print("&",end=" ")
#     for j in range(i-1):
#         print("*", end=' ')
#     print()   


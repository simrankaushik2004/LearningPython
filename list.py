#write a program to sum of all the elements of list
# a=[1,2,3,4]
# sum=sum(a)
# print(sum)


#write a program to sum of all the elements of list
# k=[9,6,5]
# x = 1
# for i in k:
#     x = x * i
# print("mul:",x)/


# hello we all are learners 


# Python program to find largest
# # number in a list
 
# # List of numbers
# list1 = [10,23,45,8]
# # list1.sort()
# # print(list1[-1])
# # Printing the maximum element
# print(max(list1))

# Python program to find smallest
def smallerelement(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min
print(smallerelement([2,1,3,4,5]))

# Python program to find largest
def maxlist(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(maxlist([2,1,3,4,5]))


list1 = [10,23,45,8]
list1.sort()
print(list1[0])

list1 = [10,23,45,8]
# # Printing the maximum element
print(min(list1))
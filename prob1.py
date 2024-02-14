from functools import reduce
numbers = '12345'
list1=[]
list1=[int(number) for number in numbers]
sum_of_numbers = reduce(lambda x, y: x + y, list1)
print(sum_of_numbers)
# for i in number:
#     sum+=int(i)
# print (sum)

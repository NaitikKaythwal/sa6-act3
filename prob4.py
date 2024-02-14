# list1 = [1,2,3,4,5,4]
# list2 = [1,3,5,7,9]

# merged_list = []
# for i in range(len(list1)):
#     if list1[i] in list2:
#         merged_list.append(list1[i])

# print(merged_list)

list1 = [1,2,3,4,5,4]
list2 = [1,3,5,7,9]
merged_list = list(filter(lambda x: x in list1, list2))
print(merged_list)


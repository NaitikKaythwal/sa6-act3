def find_maximum(numbers, compare):
    max_num=numbers[0]
    for i in numbers[1:]:
        if compare(i, max_num) > 0:
            max_num = i
    return max_num

numbers = [5, 3, 9, 2, 7, 1, 8, 4, 6]
compare = lambda x, y: x - y

max_number = find_maximum(numbers, compare)
print(max_number)


# def get_maximum(numbers):
#     max_num=numbers[0]
#     for i in numbers[1:]:
#         if i>max_num:
#             max_num=i
#     return max_num

# numbers = [5, 3, 9, 2, 7, 1, 8, 4, 6]
# max_num=get_maximum(numbers)
# print(max_num)

# def get_maximum(numbers):

# numbers = [5, 3, 9, 2, 7, 1, 8, 4, 6]
# # Use a lambda function as the sorting key
# sorted_numbers = sorted(numbers, key=lambda x: x )
# print(sorted_numbers[-1])
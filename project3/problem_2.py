def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    front, tail = input_list[0], input_list[-1]
    if number == front:
        return 0
    if number < front:
        label = tail ### 大于label，则在右边
    if number > front:
        label = front ### 小于label，则在左边
    return search(input_list, number, label, 0, len(input_list)-1)

def search(input_list, number, label, left, right):
#     print(left)
    if (left == right or left+1==right)  and number != input_list[left] and number != input_list[right]:
        return -1
        
    if label == input_list[0]:
        middle_index = (left +right) // 2
        if input_list[middle_index] == number:
            return middle_index
        if input_list[middle_index] < number and input_list[middle_index] > label:
            return search(input_list, number, label, middle_index, right)
        return search(input_list, number, label, left, middle_index)
        
    else:
        middle_index = (left +right) // 2
        if input_list[middle_index] == number:
            return middle_index
        if input_list[middle_index] > number and input_list[middle_index] <= label:
            return search(input_list, number, label,left, middle_index)
        return search(input_list, number, label,middle_index, right)        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print('—'*20,'Case1:','—'*20,)
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
print('—'*20,'Case2:','—'*20,)
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print('—'*20,'Case3:','—'*20,)
test_function([[6, 7, 8, 1, 2, 3, 4], 0])
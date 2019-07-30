def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0 = 0
    cur = 0
    next_2 = len(input_list) - 1
    while cur <= next_2:
#         print(cur)
        if input_list[cur] == 0:
            if cur == next_0:
                cur += 1
                next_0+=1
            else:
                temp = input_list[next_0]
                input_list[next_0] = 0
                input_list[cur] = temp
                next_0 += 1
            
        elif input_list[cur] == 1:
            cur += 1
        else:
            temp = input_list[next_2]
            input_list[next_2] = 2
            input_list[cur] = temp
            next_2 -= 1
#         print(input_list)
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
        
print('—'*20,'Case1:','—'*20,)
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('—'*20,'Case1:','—'*20,)
test_function([0,])
print('—'*20,'Case1:','—'*20,)
test_function([2])
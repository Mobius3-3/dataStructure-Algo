def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) < 2:
        return -1
    left = input_list[0:len(input_list)//2]
    right = input_list[len(input_list)//2:]
#     print(left, right)
    left = merge(left[0:len(left)//2],left[len(left)//2:]) if len(left)>1 else left
    right = merge(right[0:len(right)//2],right[len(right)//2:]) if len(right)>1 else right
    
    n_1, n_2 = [], []
    i,j = 0,0
    last_1 = 0
    while i < len(left):
        if j>=len(right) or left[i] >= right[j]:
            n_1.append(left[i]) if last_1 == 0 else n_2.append(left[i])
            last_1 = last_1 == 0
            i+=1
            continue
        while j<len(right) and left[i] < right[j]:
            n_1.append(right[j]) if last_1 == 0 else n_2.append(right[j])
            last_1 = last_1 == 0
            j+=1
    
    while j<len(right):        
            n_1.append(right[j]) if last_1 == 0 else n_2.append(right[j])
            last_1 = last_1 == 0
            j+=1
    n_1_int = int(''.join([str(_) for _ in n_1]))
    n_2_int = int(''.join([str(_) for _ in n_2]))
    return  [n_1_int, n_2_int]
    
def merge(left,right):
    if len(left) != 1:
#         print(left)
        left = merge(left[0:len(left)//2],left[len(left)//2:])
    if len(right) != 1:
        right = merge(right[0:len(right)//2],right[len(right)//2:])
        
    i,j=0,0
    n_1 = []
    while i < len(left):
#         print(left)
        if j>=len(right) or left[i] >= right[j]:
            n_1.append(left[i]) 
            i+=1
            continue
        while j<len(right) and left[i] < right[j] :
            n_1.append(right[j]) 
            j+=1
    while j<len(right):        
        n_1.append(right[j]) 
        j+=1
#     print(n_1)
    return n_1

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
        
print('—'*20,'Case1:','—'*20,)
test_function([[1, 2, 3, 4, 5], [542, 31]])
print('—'*20,'Case2:','—'*20,)
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
print('—'*20,'Case3:','—'*20,)
test_function([[0,1,2,3,4], [420, 31]])
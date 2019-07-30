def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
#         print('Negative number fail!')
        return -1
    return sqrt_helper(number,0,number)

def sqrt_helper(number, left, right):
    if right-left<1:
        return right // 1
    middle = ((left + right) / 2) 
#     print(middle)
    if middle ** 2 < number:
        left = middle
    elif middle ** 2 > number:
        right = middle
    else:
        return middle 
    return sqrt_helper(number, left, right)
    
print('—'*20,'Case1:','—'*20,)
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print('—'*20,'Case2:','—'*20,)
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print('—'*20,'Case3:','—'*20,)
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print('—'*20,'Case4:','—'*20,)
print ("Pass" if  (-1 == sqrt(-1)) else "Fail")
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 1:
        return -1
    min_index, max_index = 0, 0
    for i in range(1,len(ints)):
        if ints[i] > ints[max_index]:
            max_index = i
        if ints[i] < ints[min_index]:
            min_index = i
    return ints[min_index], ints[max_index]

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print('—'*20,'Case1:','—'*20,)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((-1, 10) == get_min_max([10, -1])) else "Fail") # list with two ints
print ("Pass" if ((-10, 15) == get_min_max([5, 1, 0, -1, 10, 15, 8, -10])) else "Fail")
print('—'*20,'Case2:','—'*20,)
print ("Pass" if ((5, 5) == get_min_max([5])) else "Fail") # single digit list
print('—'*20,'Case3:','—'*20,)
print ("Pass" if (-1 == get_min_max([])) else "Fail") # single digit list
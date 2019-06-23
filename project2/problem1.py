from collections import deque, OrderedDict

class LRU_Cache(object):
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.num_data = 0
        self.data = OrderedDict()
#         self.queue_key = deque()
    
    def get(self, key):
        if key in self.data:
            value = self.data.pop(key)
            self.data[key] = value
            return self.data[key]
        return -1
    
    def set(self, key, value):
        if self.num_data < self.capacity:
            if key in self.data:
                value = self.data.pop(key)
                self.data[key] = value
            else:
#                 self.queue_key.append(key)
                self.data[key] = value
                self.num_data += 1
        else:
            try:
                delete_key = next(iter(self.data.keys()))
                self.data.pop(delete_key)
    #             self.queue_key.append(key)
                self.data[key] = value
                self.num_data += 1
            except:
                print("Set Error: no cache space can be used!")
    
#     def reorder(self, key):
#         self.queue_key.remove(key)
#         self.queue_key.append(key)


### test case
print("Cases1:___________________________________________________________________________")
our_cache = LRU_Cache(5)

our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)    
our_cache.set(4,4)

print("True result of our_cache.get(1) is 1, and the output is {}.".format(our_cache.get(1)))
print("True result of our_cache.get(2) is 2, and the output is {}.".format(our_cache.get(2)))
print("True result of our_cache.get(9) is -1, and the output is {}.".format(our_cache.get(9)))

our_cache.set(5, 5)
our_cache.set(6, 6)

print("True result of our_cache.get(1) is 1, and the output is {}.".format(our_cache.get(1)))
print("True result of our_cache.get(3) is -1, and the output is {}.".format(our_cache.get(3)))


print("\nCases2:___________________________________________________________________________")
our_cache = LRU_Cache(1)

print("True result of our_cache.get(1) is -1, and the output is {}.".format(our_cache.get(1)))

print("\nCases3:___________________________________________________________________________")
our_cache = LRU_Cache(0)
our_cache.set(1,1) # set error are supposed to be printed
print("True result of our_cache.get(1) is -1, and the output is {}.".format(our_cache.get(1)))
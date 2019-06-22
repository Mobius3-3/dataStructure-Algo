class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    value_count = dict({})
    res = LinkedList()
    
    node = llist_1.head
    while node:
        if node.value in value_count:
            node = node.next
            continue
        else:
            value_count[node.value] = 1
            if res.head == None:
                res.head = Node(node.value)
            else:
                res.append(node.value)
            node = node.next
                
    node = llist_2.head
    
    while node:
        if node.value in value_count:
            node = node.next
            continue
        else:
            value_count[node.value] = 1
            if res.head == None:
                res.head = Node(node.value)
            else:
                res.append(node.value)
            node = node.next
    return res

def intersection(llist_1, llist_2):
    # Your Solution Here
    value_count = dict({})
    res = LinkedList()
    
    node = llist_1.head
    while node:
        if node.value in value_count:
            node = node.next
            continue
        else:
            value_count[node.value] = 1
            node = node.next
                
    node = llist_2.head
    
    while node:
        if node.value not in value_count:
            node = node.next
            continue
        elif value_count[node.value] == 1:
            
            if res.head == None:
                res.head = Node(node.value)
            else:
                res.append(node.value)
        value_count[node.value] += 1
        node = node.next
    return res




# Test case 1
print("Test case 1____________________________________________________________________________")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

print("\nTest case 2____________________________________________________________________________")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


print("\nTest case 3____________________________________________________________________________")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,1,1,1,1,1,2,]
element_2 = [3,3,33,3,3,3,3,3,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
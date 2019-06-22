class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        self.chr = None
    # def isLeft(self):
    #     if self.parent == None:
    #         return False
    #     if self.parent.left == self:
    #         return True
    #     return False

class Tree(object):
    def __init__(self, value=None):
        self.root = value
    
def get_freq(data):
    dict_str = dict({})
    for i in data:
        if i in dict_str:
            dict_str[i] += 1
        else:
            dict_str[i] = 1
    item = list(dict_str.items())
    item.sort(key = lambda x: x[1])
    return item

def get_code(root):
    if root.left == None and root.right == None:      
        return [root.chr]
    
    if root.left:   
        res_l = get_code(root.left)
        res_l = ['0'+item for item in res_l]
    if root.right:
        res_r = get_code(root.right)
        res_r = ['1'+item for item in res_r]
    return res_l + res_r

def huffman_encoding(data):
    item = get_freq(data)
    tree = Tree()
    if len(item) == 1:
        root = Node(item[0][1])
        root.chr = item[0][0]
        tree.root = root
    else:
        while (len(item)>=2):
            node_l = Node()
            node_r = Node()
            if type(item[0][0]) == str:
                node_l.value = item[0][1]
                node_l.chr = item[0][0]
            else:
                node_l = item[0][0]
            if type(item[1][0]) == str:
                node_r.value = item[1][1]
                node_r.chr = item[1][0]
            else:
                node_r = item[1][0]

            root = Node(node_l.value+node_r.value)
            root.left = node_l
            root.right = node_r

            item.pop(0)
            item.pop(0)
            item.append((root, root.value))
            item.sort(key=lambda x:x[1])
        tree.root = root
    
    codes = get_code(root)
    dict_codes = {}
    if len(codes) == 1:
        return len(data), tree  ### if only one character, return length of the string and tree
    else: 
        for i in codes:
            dict_codes[i[-1]] = i[:-1]
        code=""
        for i in data:
            code += dict_codes[i]
    return code, tree
    
def huffman_decoding(data, tree):
    root = tree.root
    if root.left == None and root.right == None:
        return root.chr * data
    codes = get_code(root)
    dict_codes = {}
    dict_decodes = {}
    for i in codes:
        dict_codes[i[-1]] = i[:-1]
        dict_decodes[i[:-1]] = i[-1]
    index_start = 0
    max_len = max([len(item) for item in list(dict_codes.values())])
    
    decode = ''
    while (index_start<len(data)):
        for length in range(1,max_len+1):
            if data[index_start: index_start+length] in list(dict_codes.values()):
                decode += dict_decodes[data[index_start:index_start+length]] 
                index_start += length
                break
    return decode
    

print("Case1:____________________________________________________________________________")
import sys
a_great_sentence = "it's a very very very very very very very very very very very very very very \
                    very very very very very very very very very very very very very long sentence"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))


encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

print("Case2:____________________________________________________________________________")
a_great_sentence = "qwertyuiopasdfghklzxcvbnm" # no same character

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))


encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

print("Case3:____________________________________________________________________________")
a_great_sentence = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))


encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}
        
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
    
    def suffixes_helper(self, suffix):
        ## Helper method to get all the suffixes from the TrieNode
        if self.is_word:
            yield suffix 
            
        for i in self.children:
            yield from self.children[i].suffixes_helper(suffix + i)
        
    def suffixes(self, suffix = ''):
        suffixes_generator = self.suffixes_helper(suffix)
        output = []
        for i in suffixes_generator:
            output.append(i)
        return output
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:   
                return
            current_node = current_node.children[char]

        return current_node
    

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
# Case when the Trie has a TrieNode with the prefix 'f'
# Output -  TrieNode with the prefix 'f' 
print('—'*20,'Case1:','—'*20,)
print('Pass' if MyTrie.find('f').suffixes()==['un', 'unction', 'actory'] else 'Fail') 

# returns all the suffixes with the prefix 'a' which is ['nt', 'nthology', 'ntagonist', 'ntonym']
print('Pass' if MyTrie.find('a').suffixes() == ['nt', 'nthology', 'ntagonist', 'ntonym'] else 'Fail') 

# Case when looking for siffix of empty string prefix then it returns all the words in the Trie
# Output - ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
print('Pass' if MyTrie.find('').suffixes()==['ant', 'anthology', 'antagonist', 'antonym', 'fun',\
        'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod'] else 'Fail'
)

# Case when prefix is empty string
# output is None
print('—'*20,'Case2:','—'*20,)
print('Pass' if MyTrie.find('h')== None else 'Fail')

# Case when prefix is empty string
# Output - root of the Trie
print('—'*20,'Case3:','—'*20,)
try:
    print(MyTrie.find('g').suffixes())
except AttributeError:
    
    print('Pass',"Please insert words into the Trie to search for suffixes.")
    
# Case when trying to get the suffixes for a prefix which is not in the Trie
# Output - AttributeError: 'NoneType' object has no attribute 'suffixes'
# Hence, given custom error
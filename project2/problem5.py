import hashlib
import datetime, time


class Block:
    def __init__(self, data):
        self.timestamp = None
        self.data = data
        self.previous_hash = None
        self.hash = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        if self.previous_hash != None:
            hash_str = (str(self.timestamp) + str(self.data) ).encode('utf-8')
        else:
            hash_str = (str(self.timestamp) + str(self.data) ).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.get_generic_block()]
        self.len = 1
#         self.tail_block = Block(time.time(),'Generic block generated.', None)
    
    def get_generic_block(self):
        generic_block = Block('Generic block generated.')
        generic_block.timestamp = time.time()
        generic_block.hash = generic_block.calc_hash()
        return generic_block
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self, block):
        last_block = self.get_last_block()
        previous_hash = last_block.hash
        new_block = block
        new_block.timestamp = time.time()
#         print(str(new_block.timestamp))
        new_block.previous_hash = last_block.hash
        new_block.hash = new_block.calc_hash()
        self.chain.append(new_block)
        self.len += 1
    
    def print_blockchain(self):
        print('Blockchain in reversed order:\n')
        for i in range(self.len):
            index = self.len-i-1
            if index == 0:
                print("generic block printed:")
                self.print_block(self.chain[index])
            elif self.chain[index].previous_hash == self.chain[index-1].hash:
                print("block {} printed:".format(index+1))
                self.print_block(self.chain[index])
            else:
                print("Error: block failed hash validation!")
                break
            
    def print_block(self, block):
        print('timestamp: {}\ndata: {}\nprevious hash: {}\ncurrent hash: {}\n'.format(
            block.timestamp,
            block.data,
            block.previous_hash,
            block.hash))
#         time.sleep(0.1)

print('Test Case 1____________________________________________________________________')
# Create a blockchain
my_blockchain = Blockchain()

# Generate root block
my_data = "First added block"

root = Block(my_data)
# add the root block to the chain
my_blockchain.add_block(root)

# Generate second block
my_data = "Second added block"
block = Block(my_data)

# add the second block to the chain
my_blockchain.add_block(block)

# Generate third block
my_data = "Third added block"
block = Block(my_data)

# add the third block to the chain
my_blockchain.add_block(block)
my_blockchain.print_blockchain()

print('\nTest Case 2____________________________________________________________________')
# Create a blockchain
my_blockchain = Blockchain()
my_blockchain.print_blockchain()

print('\nTest Case 3____________________________________________________________________')
# Create a blockchain
my_blockchain = Blockchain()

# Generate root block
my_data = "root data"

root = Block(my_data)
# add the root block to the chain
my_blockchain.add_block(root)

# Generate second block
my_data = "1234567890"
block = Block(my_data)

# add the second block to the chain
my_blockchain.add_block(block)

# Generate third block
my_data = "1234567890"
block = Block(my_data)

# add the third block to the chain
my_blockchain.add_block(block)
my_blockchain.print_blockchain()